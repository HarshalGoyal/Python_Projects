#this is the code for taking voice input from user and searching that on wiki and responding with the summary from wiki
import wikipedia
import pyttsx3
import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening")
    r.pause_threshold = 2
    audio = r.listen(source)

    try:
        print("Recognising")
        qurey = r.recognize_google(audio, language='en-in')
        print(f"user input:{qurey}\n ")
        wikipedia.search(r.recognize_google(audio, language='en-in'))

        engine = pyttsx3.init()

        res=wikipedia.summary(r.recognize_google(audio, language='en-in'))

        print("According to wikipedia : %s"%res)

        engine.say(res)
        engine.runAndWait()

    except Exception as e:

        print("please re Run the program")
        





