import pyttsx3 
import speech_recognition as sr
import random
import webbrowser
import datetime
engine = pyttsx3.init()


voices = engine.getProperty('voices') # getting details of current voice
engine.setProperty('voice', voices[1].id) 
for voice in voices:
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate",150)
   


def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def command():  
    content = " "
    while  content == " ":
    # obtain audio from the microphone
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Say something!")
         audio = r.listen(source)

     try:
         content = r.recognize_google(audio,language='en-in')
         print("You said.........." + content )
     except Exception as e:
      print ("please try again...")
      content= " "
    return content
# Main loop 
while True:
    request= command().lower()
    if "hello" in request:
        speak("welcome, how can i help you.")
    elif "play music" in request:
     speak("playing music")
     #song = (1,2,3,4)
     song = random.randint (1,3)
     if song == 1:
        webbrowser.open("https://youtu.be/6rCCadPzDzM?list=RD6rCCadPzDzM")
     elif song==2:
        webbrowser.open("https://youtu.be/0WziMtAB2hE?list=RD6rCCadPzDzM")
     elif song==3:
        webbrowser.open("https://youtu.be/ag3ENMEV89o?list=RD6rCCadPzDzM")
    elif "say time" in request:
       now_time= datetime.datetime.now().strftime("%H:%M")
       speak("current time is " + str(now_time))
    elif "day date" in request:
       now_date = datetime.datetime.now().strftime("%d:%m")
       speak("current date is "+ str(now_date))

     #main_process()                  

