from googletrans import Translator
import re
import copy
from whisper.utils import get_writer

def translatEnglishByWhisper(model, audioFilePath, path, srtFileName, object):
    object.chageToGrey("en", "SRT")
    result = model.transcribe(audioFilePath, task="translate")
    srt_writer = get_writer("srt", path)
    srt_writer(result, srtFileName)
    object.chageToGreen("en", "SRT")


def translate_srt(original_file, output_file, output_lang, object):
    object.chageToGrey(output_lang, "SRT")

    with open(original_file, 'r', encoding='utf-8') as file:
        srt = file.read()

    subtitels = re.split(r'\n\s*\n', srt)

    translator = Translator()

    translated_subtitels = []

    for subtitle in subtitels:
        lines = subtitle.split('\n')
        if len(lines) >= 3:
            text_to_translate = '\n'.join(lines[2:])
            translated_text = translator.translate(text_to_translate, dest=output_lang).text

            translated_subtitle = f'{lines[0]}\n{lines[1]}\n{translated_text}\n'
            translated_subtitels.append(translated_subtitle)


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(translated_subtitels))
    
    object.chageToGreen(output_lang, "SRT")


def translate_srt2(output_file, output_lang, result, srt_directory, object):
    object.chageToGrey(output_lang, "SRT")
    copyResult = copy.deepcopy(result)
    segments = result["segments"]
    translator = Translator()
    text_to_translate = ""
    translated_subtitels = []

    for segment in segments:
        text_to_translate += " (0)" + segment["text"].lstrip(" ")

    text_to_translate_with_dots = ""
    for char in text_to_translate:
        if 'A' <= char <= 'Z':
            text_to_translate_with_dots += '.' + char
        else:
            text_to_translate_with_dots += char
    text_to_translate_with_dots = text_to_translate_with_dots[5:]

    
    sentences = text_to_translate_with_dots.split('.')
    sentences = [item for item in sentences if item]
    translated_text = ""
    for sentence in sentences:
        translated_text += translator.translate(sentence, dest=output_lang).text
        
    if output_lang == "zh-CN":
        translated_subtitels = re.split(r'（0）', translated_text)
    else:
        translated_subtitels = re.split(r'\(0\)', translated_text)

    a = 0
    existError = False
    segments = copyResult["segments"]
    for segment in segments:
        try:
            segment["text"] = translated_subtitels[a]
            a += 1
        except:
            print("Did miss a line")
            existError = True

    srt_writer = get_writer("srt", srt_directory)
    srt_writer(copyResult, output_file)

    if existError:
        object.chageToRed(output_lang, "SRT")
    else:
        object.chageToGreen(output_lang, "SRT")
