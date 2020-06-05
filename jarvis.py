# Import the required module for text 
# to speech conversion 
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().date)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning vishnu")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon vishnu")
    elif hour >=18 and hour <24:
        speak("Good evening vishnu")
    else:
        speak("Good night vishnu")

    speak("Jarvis at your service. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vishnu2015189@gmail.com','15903570')
    server.sendmail('vishnu2015189@gmail.com',to, content)


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Vishnu/Pictures/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'send email' in query:
                try:
                    speak("What should i say?")
                    content = takeCommand()
                    to = 'vardhanv714@gmail.com'
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Unable to send the EMAIL")

        elif 'search in chrome' in query:
            speak("what should i search")
            chromepath = 'C:/Users/Vishnu/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play song' in query:
            songs_dir = 'C:/Users/Vishnu/Music'
            songs= os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'youtube' in query:
            speak("Opening youtube...")
            chromepath = 'C:/Users/Vishnu/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab('youtube.com')

        elif 'hi'  in query:
            speak('Hello')

        elif 'how are you' in query:
            speak('i am good, what about?')
            response = takeCommand()
            if response == good or response == fine :
                speak("That's great to hear")
            else:
                speak("i am sorry for that")
        
        elif 'age'  in query:
            speak("i am a small baby")

        elif 'created'  in query:
            speak("My master vishnu created me")



        elif 'offline' or 'bye' in query:
            speak("Bye sir see you soon")
            quit()



        

        

    




