import speech_recognition as sr
import pyttsx3
from tkinter import *
import tkinter as tk
import pyjokes
import webbrowser
import os
import datetime

yt_url = "https://www.youtube.com"
ggl_url = "https://www.google.com"
root = tk.Tk()
jokes = (pyjokes.get_joke())

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx3.init()

    with mic as source:
        audio = recognizer.listen(source)

    output = recognizer.recognize_google(audio, language="en-US")

    print(output)

    if output == "hello":
        engine.say("hello")
        engine.runAndWait()
        listen()

    if output == "what is your name":
        engine.say("my name is Diamond and i am your virtual assistant")
        engine.runAndWait()
        listen()

    if output == "what's your name":
        engine.say("my name is Diamond and i am your virtual assistant")
        engine.runAndWait()
        listen()

    if output == "tell me a joke":
        engine.say(jokes)
        engine.runAndWait()
        listen()

    if output == "open YouTube":
        engine.say("opening YouTube")
        engine.runAndWait()
        webbrowser.open_new(yt_url)
        listen()

    if output == "open Google":
        engine.say("opening Google")
        engine.runAndWait()
        webbrowser.open_new(ggl_url)
        listen()

    if output == "open Chrome":
        engine.say("opening chrome")
        engine.runAndWait()
        os.system("start chrome.exe")
        listen()

    if output == "open Steam":
        engine.say("opening steam")
        engine.runAndWait()
        os.system("start steam.exe")
        listen()

class usr_input():
    root.geometry("500x400")
    root.title("diamond assistant alpha V1.0")
    button1 = Button(text="start virtual assistant", command=listen)
    button1.pack()
    root.mainloop()

