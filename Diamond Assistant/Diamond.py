        ###############################################################################
        #                                                                             #
        #                    Diamond Virtual Assistant alpha v1.1                     #
        #                                                                             #
        ###############################################################################

# updated: 14:20 friday 2021-05-14.
# feel free to upgrade / fork.

import datetime
import speech_recognition as sr
import pyttsx3
from tkinter import *
import tkinter as tk
import pyjokes
import webbrowser
import os
from datetime import date, time
import random

memel = "https://preview.redd.it/8vsh7q05q8y61.jpg?width=640&crop=smart&auto=webp&s=850dbd40d2cd76a04f05ed2599d0669ff9cae42e"
meme2 = "https://preview.redd.it/ftyebodmj8y61.jpg?width=640&crop=smart&auto=webp&s=0657f6366c074f29b8fafaad46d066ce661e27a8"
yt_url = "https://www.youtube.com"
ggl_url = "https://www.google.com"
root = tk.Tk()
launch_btn = PhotoImage(file="images/launch.png")
exit_button = PhotoImage(file="images/exit.png")
commands_button = PhotoImage(file="images/commands.png")
website_button = PhotoImage(file="images/website.png")
logo = PhotoImage(file="images/logo.png")
jokes = (pyjokes.get_joke())

def website_open():
    webbrowser.open("https://sawano.000webhostapp.com")

def commands():
    os.system("start commands.txt")

def exit():
    quit()

def listen():
    input("Press enter to listen..")
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

    if output == "start Chrome":
        engine.say("opening chrome")
        engine.runAndWait()
        os.system("start chrome.exe")
        listen()

    if output == "what's the time":
        e = datetime.datetime.now()
        engine.say("The time is %s:%s:" % (e.hour, e.minute))
        engine.runAndWait()
        listen()

    if output == "what's the date":
        todays_date = date.today()
        engine.say("todays date is")
        engine.say(todays_date)
        engine.runAndWait()
        listen()

    else:
        engine.say("I didn't understand that but maybe i do in future updates !")
        engine.runAndWait()
        listen()

class usr_input():
    root.geometry("600x700")
    root.title("diamond assistant alpha V1.0")
    root.configure(bg="white")
    Label(image=logo, bg="white").pack()
    Label(text="Diamond Alpha", fg="purple", bg="white", 
    font="Courier 20").pack()
    Label(text=" ", font="Arial 30", bg="white").pack()
    button1 = Button(image=launch_btn, command=listen, 
    bg="white", borderwidth="0")
    button2 = Button(image=exit_button, bg="white", 
    borderwidth="0", command=exit)
    button3 = Button(image=commands_button, command=commands, 
    bg="white", borderwidth="0")
    button4 = Button(image=website_button, command=website_open, 
    bg="white", borderwidth="0")
    button1.pack()
    Label(text=" ", font="Arial 15", bg="white").pack()
    button2.pack()
    Label(text=" ", font="Arial 15", bg="white").pack()
    button3.pack()
    Label(text=" ", font="Arial 15", bg="white").pack()
    button4.pack()
    root.mainloop()

