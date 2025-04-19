import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

  

#this will speak the string
def speak(text):
    engine.say(text)
    engine.runAndWait()


#this function will wishes me
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak(f"good morning {name} how may i help you")
    elif hour >=12 and hour <18:
        speak(f"good afternoon {name} how may i help you")
    else:
        speak(f"good evening {name} how may i help you")
    #speak("i am your assistant how may i help you?")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("pramodnagaral@gmail.com",'178ec15031')
    server.sendmail("pramodnagaral@gmail.com", to, content)
    server.close()


def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in') #indian english
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again please")
        query = None
    return query
 

#main program starts here
print("enter your name : ")
name = input()
print("Initialization jarvis")
speak("Initializing jarvis")
wishme()
querry = takecommand()

if 'wikipedia' in querry.lower():
    speak(f'ya.. well{name} i am searching in wikipedia')
    query = querry.replace("wikipedia","")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)
elif 'open youtube' in querry.lower():
    url ="www.youtube.com"
    # Windows
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
    #chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.open(url)

elif 'open google' in querry.lower():
    url="www.google.com"
    webbrowser.open(url)


elif 'open hackerrank' in querry.lower():
    url="www.hackerrank.com"
    webbrowser.open(url)

elif 'the time' in querry.lower():
    strtimr = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{name} the time is {strtimr}")
elif 'open code' in querry.lower():
    codepath = "C:\\Users\\gangadhar nagaral\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)
elif 'python tutorials' in querry.lower():
    tutopath = "E:\\python"
    os.startfile(tutopath)
elif 'syllabus' in querry.lower():
    salpath = "F:\\6th sem"
    os.startfile(salpath)
elif 'email to pramod' in querry.lower():
    try:
        print('what should i send')
        speak('what should i send')
        content = takecommand() 
        to = 'pramodnagaral@gmail.com'
        sendemail(to,content)
        speak("email has been sent successfully")
    except Exception as e:
        print(e)