import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import wikipedia 


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")  
    speak(year)  

def wishme():
    speak("welcome back iam your friend jarvis")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >=12 and hour <18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")   
    else:
        speak("Good night")

       
    speak("how can i help you ?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        print("Recoginizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again")
        return "None"
    return query

   

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("monijaya33@gmail.com", "monishaj")
    server.sendmail("monijaya33@gmail.com", to, content)
    server.close()



def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshots.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage) 

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent )   

def jokes():
    speak(pyjokes.get_joke())  





if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()  
        elif"send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "monijaya33@gmail.com"
                sendmail(to, content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("unable to send the message") 
        elif "search in chrome" in query:
            speak("what should i search in chrome?")
            chromepath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t l")
        elif "resart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = "C://Users//jvini//Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()   
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("done")

        elif "cpu" in query:
            cpu()    
        elif "joke" in query:
            jokes() 
        
        elif"alarm" in query:
            speak("enter the time !")
            time=input(":enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strfttime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up !")
                    speak("alarm closed!")

                elif now>time:
                    break
        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)       



               
            






        



