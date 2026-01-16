import pyttsx3 
import speech_recognition as sr
engine = pyttsx3.init()

voices = engine.getProperty('voices') # getting details of current voice
engine.setProperty('voice', voices[1].id) 
for voice in voices:
    engine.setProperty('voice', voices[0].id)
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
         content = r.recognize_google(audio,language='en-IN')
         print("You said.........." + content )
     except Exception as e:
      print ("please try again...")
    return content
while True:
    request= command()
    if request:
     print(request)




# speak ("how are you")

