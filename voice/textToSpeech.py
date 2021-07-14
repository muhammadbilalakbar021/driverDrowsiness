from pygame import mixer
from gtts import gTTS
import os

# os.add_dll_directory('app')
path = "welcome.mp3"


def TextToSpeech(text):
    language = 'en'
    counter = 1
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome"+str(counter)+".mp3")
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
    counter = counter + 1
    # time.sleep(5)
def textToSpeech(mytext):
    counter = 1
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome"+str(counter)+".mp3")
    os.system("welcome.mp3")