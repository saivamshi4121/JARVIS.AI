import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("this is jarvis . how can i help you")


def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)  # Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance, which it returns.
    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n") 
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('palamurivamshi2005@gmail.com','palamurisaivamshi123456')
    server.sendmail('palamurisaivamshi2005@gmail.com',to,content)
    server.close()




if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query= takeCommand().lower()

    #logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('Sreaching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music from youtube' in query:
            webbrowser.open("https://www.youtube.com/watch?v=XLqmL9cPN1E&list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g&index=2")
        elif 'play news from youtube' in query:
            webbrowser.open("https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw")
        elif'play music' in query:
            music_dir = 'D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir ,the time is {strTime}")
        elif 'open code ' in query:
            codePath="C:\\Users\\palam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to vamshi' in query:
            try:
                speak("what should i say?")
                content =takeCommand()
                to="palamurisaivamshi2005@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry this momnet i cant send")

            

