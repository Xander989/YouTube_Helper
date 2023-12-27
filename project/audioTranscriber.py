import whisper
from whisper.utils import get_writer
import srtTranslator
import audioSpeaker
import os


directory = ""
srt_directory = "/SRT/"
audio_directory = "/audio/"
audioFilePath = ""
srtFileName = "Original"
srtFilePath = directory + srt_directory + srtFileName + ".srt"




def transcribeAudio(object):
    os.makedirs(os.path.dirname(directory + srt_directory), exist_ok=True)
    os.makedirs(os.path.dirname(directory + audio_directory), exist_ok=True)
 
    model = whisper.load_model(object.listOfModels.currentText())
    result = model.transcribe(audioFilePath)
    srt_writer = get_writer("srt", directory + srt_directory)
    srt_writer(result, srtFileName)

    for checkBoxe in object.checkBoxes:
        if checkBoxe.isChecked():
            if checkBoxe.objectName() == "en" and object.enWhisperChooser.currentText() == "Yes":
                srtTranslator.translatEnglishByWhisper(model, audioFilePath, directory + srt_directory, checkBoxe.text(), object)
                

            elif object.typesOfTranslator.currentText() == "Line by line":
                srtTranslator.translate_srt(directory + srtFilePath, directory + srt_directory + checkBoxe.text() + ".srt", checkBoxe.objectName(), object)
                

            elif object.typesOfTranslator.currentText() == "Sentence":
                srtTranslator.translate_srt2(directory + srt_directory + checkBoxe.text(), checkBoxe.objectName(), result, directory + srt_directory, object)
            
            if object.ctreateVoiceSwitch.currentText() == "Yes":
                audioSpeaker.makeAudio(result, checkBoxe.objectName(), checkBoxe.text(), directory + audio_directory, object)
