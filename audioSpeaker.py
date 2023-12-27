from transformers import AutoProcessor, AutoModel
import scipy
from googletrans import Translator
import nltk
from pydub import AudioSegment
import os

from bark import generate_audio, SAMPLE_RATE




def makeAudio(result, output_lang, fileName, output_file_path, object):
    object.chageToGrey(output_lang, "Audio")
    combined_audio = AudioSegment.silent()
    nltk.download('punkt')
    processor = AutoProcessor.from_pretrained("suno/bark")
    model = AutoModel.from_pretrained("suno/" + object.typesOfVoiceModels.currentText())
    translator = Translator()
    sentences = nltk.sent_tokenize(result["text"])
    text_to_spech = []
    for sentence in sentences:
        text_to_spech.append(translator.translate(sentence, dest=output_lang).text)

    print(text_to_spech)
    a = 0
    for sentence in text_to_spech:
        inputs = processor(
        text=[sentence],
        return_tensors="pt",
        )
        
        speech_values = model.generate(**inputs, do_sample=True)
        scipy.io.wavfile.write(output_file_path + fileName + str(a) + ".wav", rate=SAMPLE_RATE, data=speech_values.cpu().numpy().squeeze())
        a += 1

    for i in range(a):
        file_name = output_file_path + fileName + str(i) + ".wav"
        audio_segment = AudioSegment.from_wav(file_name)
        combined_audio += audio_segment

    combined_audio.export(output_file_path + fileName + ".wav", format="wav")

    for i in range(a):
        os.remove(output_file_path + fileName + str(i) + ".wav")

    object.chageToGreen(output_lang, "Audio")

    
    
    
    




