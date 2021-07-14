import speech_recognition as sr

from voice.Chat.ProgramYMain import ChatBot
from voice.textToSpeech import TextToSpeech, textToSpeech

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(ChatBot(query))
        print(f"user said: {query}\n")
        textToSpeech(ChatBot(query))
    except Exception as e:
        print("Miss stark couldn't recognize what you said, speak once more.")
