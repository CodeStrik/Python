import speech_recognition as sr
import pyttsx3
import pywhatkit

name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec


def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)


run()
