import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import requests
import tkinter as tk
from tkinter import StringVar
from PIL import Image, ImageTk
import threading
import time
from tkinter import ttk

# Text-to-speech setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Reminder storage
reminders = []

# Speak function
def speak(text):
    switch_animation("speaking")
    status_var.set(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    switch_animation("listening")

# Recognize voice
def recognize_speech():
    switch_animation("listening")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_var.set("🎤 Listening...")
        window.update()
        audio = r.listen(source)

        try:
            status_var.set("🔎 Recognizing...")
            window.update()
            query = r.recognize_google(audio, language='en-in')
            command_var.set(f"🗣️ You said: {query}")
            return query.lower()
        except Exception:
            status_var.set("❌ Sorry, I didn't catch that.")
            return ""

# Greet user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")

# Get weather
def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url)
        if res.status_code == 200:
            speak(res.text)
        else:
            speak("Couldn't fetch weather right now.")
    except:
        speak("Something went wrong.")

# Reminder thread
def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for reminder in reminders[:]:
            if reminder['time'] == now:
                speak(f"Reminder: {reminder['task']}")
                reminders.remove(reminder)
        time.sleep(30)

threading.Thread(target=check_reminders, daemon=True).start()

# Voice toggle
current_voice = 0
def change_voice():
    global current_voice
    current_voice = (current_voice + 1) % len(voices)
    engine.setProperty('voice', voices[current_voice].id)

# Theme toggle
def toggle_theme():
    style.theme_use("alt" if style.theme_use() == "clam" else "clam")

# Main assistant logic
def run_assistant():
    greet()
    while True:
        query = recognize_speech()

        if not query:
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, no results found.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'play music' in query:
            speak("Which song should I play?")
            song = recognize_speech()
            if song:
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            path = "C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'weather' in query:
            speak("Which city?")
            city = recognize_speech()
            if city:
                get_weather(city)

        elif 'search' in query:
            speak("What should I search for?")
            term = recognize_speech()
            if term:
                webbrowser.open(f"https://www.google.com/search?q={term}")

        elif 'open folder' in query:
            speak("Which folder path should I open?")
            folder_path = recognize_speech()
            if folder_path:
                try:
                    os.startfile(folder_path)
                except:
                    speak("Can't open the folder. Please check the path.")

        elif 'set reminder' in query:
            speak("What should I remind you about?")
            task = recognize_speech()
            speak("At what time? Say in HH:MM format.")
            rtime = recognize_speech()
            reminders.append({'task': task, 'time': rtime})
            speak(f"Reminder set for {rtime}")

        elif 'change voice' in query:
            change_voice()
            speak("Voice changed")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            window.destroy()
            break

        elif 'search' in query :
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=3)
                speak("According to Search Results:")
                speak(result)
            except:
                speak("Sorry, no results found.")

        else:
            speak("Sorry, I don't understand that.")

# GUI Setup
window = tk.Tk()
window.title("Adak's Assistant")
window.geometry("900x700")
window.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Background frame
frame = ttk.Frame(window, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

command_var = StringVar()
status_var = StringVar()

# Title
ttk.Label(frame, text="✨ AI Voice Assistant ✨", font=("Helvetica", 20, "bold")).pack(pady=10)

# Command and Status displays
ttk.Label(frame, textvariable=command_var, font=("Helvetica", 14), foreground="blue").pack(pady=5)
ttk.Label(frame, textvariable=status_var, font=("Helvetica", 14), foreground="green").pack(pady=5)

# GIF animation for assistant states
lady_label = ttk.Label(frame)
lady_label.pack(pady=20)

listening_frames = []
speaking_frames = []
current_anim = "listening"

# Load GIFs for both states
# Load GIFs for both states and resize frames
def load_gifs():
    global listening_frames, speaking_frames
    frame_size = (300, 300)  # Resize to this size

    for gif_path, frame_list in [("lady_listening.gif", listening_frames), ("lady_speaking.gif", speaking_frames)]:
        try:
            img = Image.open(gif_path)
            while True:
                frame = img.copy().resize(frame_size, Image.ANTIALIAS)
                frame_list.append(ImageTk.PhotoImage(frame))
                img.seek(len(frame_list))
        except EOFError:
            continue
        except Exception as e:
            print(f"Couldn't load {gif_path}:", e)


# Switch animation between listening and speaking
def switch_animation(mode):
    global current_anim
    current_anim = mode

# Animate gif based on state
def animate_gif():
    index = 0
    def update():
        nonlocal index
        frames = listening_frames if current_anim == "listening" else speaking_frames
        if frames:
            frame_img = frames[index % len(frames)]
            lady_label.configure(image=frame_img)
            lady_label.image = frame_img
            index += 1
        window.after(100, update)
    update()

load_gifs()
animate_gif()

# Buttons
btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="🎧 Start Listening", command=lambda: threading.Thread(target=run_assistant, daemon=True).start()).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="🎨 Toggle Theme", command=toggle_theme).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="🔄 Change Voice", command=change_voice).grid(row=0, column=2, padx=10)

window.mainloop()
