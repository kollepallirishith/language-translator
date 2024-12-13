from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Language dictionary
dic = ('afrikaans', 'af', 'albanian', 'sq', 
       'amharic', 'am', 'arabic', 'ar', 
       'armenian', 'hy', 'azerbaijani', 'az', 
       'basque', 'eu', 'belarusian', 'be', 
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 
       'bg', 'catalan', 'ca', 'cebuano', 
       'ceb', 'chinese (simplified)', 'zh-cn', 
       'chinese (traditional)', 'zh-tw', 
       'croatian', 'hr', 'czech', 'cs', 'danish', 
       'da', 'dutch', 'nl', 'english', 'en', 
       'french', 'fr', 'german', 'de', 'greek', 'el',
       'hindi', 'hi', 'kannada', 'kn', 'telugu', 'te', 'tamil', 'ta') 

def takecommand():
    """Takes audio input from the microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"The User said: {query}")
            return query
        except Exception:
            print("Could not understand audio. Please try again.")
            return None

def destination_language():
    """Prompts user to select a destination language."""
    print("Enter the language to convert to (e.g., Hindi, English):")
    to_lang = takecommand()
    if to_lang:
        to_lang = to_lang.lower()
    return to_lang

# Main Logic
query = takecommand()
while not query:
    query = takecommand()

to_lang = destination_language()
while not to_lang or to_lang not in dic:
    print("Language not recognized. Try again.")
    to_lang = destination_language()

# Translate
to_lang_code = dic[dic.index(to_lang) + 1]
translator = Translator()

try:
    text_to_translate = translator.translate(query, dest=to_lang_code)
    text = text_to_translate.text
    print(f"Translated Text: {text}")

    # Text-to-Speech
    speak = gTTS(text=text, lang=to_lang_code, slow=False)
    speak.save("captured_voice.mp3")
    playsound("captured_voice.mp3")
    os.remove("captured_voice.mp3")
except Exception as e:
    print(f"Translation failed: {e}")
