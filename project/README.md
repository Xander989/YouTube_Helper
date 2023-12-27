# YouTube Helper by Aleksandr Voronkov
#### Video Demo:  https://youtu.be/U3_xSdkkGpA
#### Description:
The main idea behind my project is to provide YouTube bloggers with a quick and high-quality solution for adding subtitles to their existing videos in different languages. Additionally, the project utilizes AI to generate new audio speech files in these languages, enabling bloggers to share their videos on a global scale. The project consists of four essential files: `main.py`, `audioTranscriber.py`, `srtTranslator.py`, and `audioSpeaker.py`, along with an "icons" folder containing additional images for the program's appearance.

- `main.py` creates the program window using the PyQt5 library. Once the window is created, it awaits user input. Within the window, users can select a file for transcription and subsequent translation/voicing, as well as choose a folder to save the files. By default, the program saves everything in its own folder.

- Users have the option to select the "Whisper" model, the translation method for SRT files, voice models, target languages, translation methods (especially for the English language), and the active functionality of voicing. Pressing the "Start" button triggers the program to check if the user has chosen a file. If yes, it proceeds to execute the next function from the `audioTranscriber.py` file.

- `audioTranscriber.py` creates an SRT subtitle file using the OpenAI library "Whisper" and runs a function to translate and voice them if the user has enabled these options in checkboxes. If any language for translation was activated, the user can choose one of three functions for translating:
  1. **Line-by-line translating:** Translates each line of existing subtitles, saves it to a new SRT file.
  2. **Sentence translating:** Creates sentences from existing subtitles, translates them, and attempts to place them into a new SRT file while considering existing time breakdowns. This method translate better than "Line by line" but may occasionally produce errors, indicated by a red icon opposite the language.
  3. **Whisper translation (English only):** Utilizes the functionality of the "Whisper" library for English translation.

- If the user has enabled voicing, the program initiates a function from the `audioSpeaker.py` file. In this file, the "transformers" library and the "Bark" voice model and processor are used to create a voice. The original text is divided into sentences, translated into the target language, and passed to the voice model. WAV files are created for each sentence, concatenated, and compiled into a final WAV file containing all sentences.

In summary, users obtain ready-to-use SRT and audio files that can be utilized as needed.