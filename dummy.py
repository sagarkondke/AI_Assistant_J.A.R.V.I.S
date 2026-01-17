import pyttsx3
import speech_recognition as sr
import random
import webbrowser

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        content = r.recognize_google(audio, language='en-in')
        print("You said:", content)
        return content
    except sr.UnknownValueError:
        print("Could not understand")
        return ""
    except sr.RequestError:
        print("Speech service error")
        return ""

while True:
    request = command().lower()

    if "hello" in request:
        speak("Welcome, how can I help you")

    elif "play music" in request:
        speak("Playing music")
        song = random.randint(1, 3)

        if song == 1:
            webbrowser.open("https://youtu.be/6rCCadPzDzM")
        elif song == 2:
            webbrowser.open("https://youtu.be/0WziMtAB2hE")
        elif song == 3:
            webbrowser.open("https://youtu.be/ag3ENMEV89o")
