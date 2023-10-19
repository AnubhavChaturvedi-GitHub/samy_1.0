import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty( 'rate',170)
def speak(Audio):
    print(" ")
    print (f": {Audio}")
    engine . say (Audio)
    print(" ")
    engine.runAndWait ()

