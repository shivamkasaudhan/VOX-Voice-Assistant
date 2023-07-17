import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shivamkasaudhan266@gmail.com', 'password')
    server.sendmail('shivamkasaudha266@gmail.com',to, content)
    server.close()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    elif hour>=18 and hour<20:
        speak("Good Evening Sir")
    else:
        speak("Good nIght Sir")
    speak("I am vox. How may I help you")
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Can you repeat sir.")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logics 
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query= query.replace("wikipedia","")
            results =wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'play music' in query:
            music_dir='C:\\zz  assignment'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath= "C:\\Users\\ASUS\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open brave' in query:
            bravepath= "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
        elif 'open chrome' in query:
            chromepath= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif 'open teams' in query:
            teamspath= "C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
            os.startfile(teamspath)
        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")
        elif 'who are you' in query:
            speak("Sir, i am vox Your personal voice assistant and I try to make your work easy.")
        elif 'email to shivam' in query:
            try:
                speak("what should i say?")
                content= takeCommand()
                to= "shivamkasaudhan266@gmail.com"
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to send this email")
        elif 'quit' in query:
            exit()