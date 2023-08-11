import sys
from AI.Listen import listen
from AI.speak import speak
import tkinter as tk
from AI.brain import ReplyBrain, ReplyQuestion
import wikipedia
import pywhatkit
import datetime
import pyautogui as pau
from time import sleep
import GUI.maingui as mg


class Commands:
    def __init__(self):
        self.ans1 = ""
        self.query1 = ""

    def command(self):
        co = Commands()
        lis = listen()
        while True:
            query = lis.Listen()

            if query is None:
                lis.Listen()
            else:
                query = query.lower()
                co.query1 = query
                print(query)
                if 'wikipedia' in query:
                    speak("searching in wikipedia,please wait...")
                    query = query.replace("wikipedia", "")
                    query = query.replace("who is", "")
                    results = wikipedia.summary(query, 2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("youtube")
                    sleep(2)
                    pau.press("enter")

                elif 'open chrome' in query or 'open google' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("chrome")
                    sleep(2)
                    pau.press("enter")

                elif 'time' in query:
                    time = datetime.datetime.now().strftime("%H:%M:%p")
                    print(time)
                    speak("Sir,Time is" + time)

                elif 'open python' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("idle")
                    sleep(2)
                    pau.press("enter")

                elif 'open vs code' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("vscode")
                    sleep(2)
                    pau.press("enter")

                elif 'youtube' in query:
                    query = query.replace("youtube", "")
                    pywhatkit.playonyt(query)

                elif 'open files' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("file Explorer")
                    sleep(2)
                    pau.press("enter")

                elif 'open settings' in query:
                    pau.press('win')
                    sleep(1)
                    pau.write("settings")
                    sleep(2)
                    pau.press("enter")

                elif 'what is' in query:
                    ans = ReplyQuestion(query)
                    co.ans1 = ans
                    speak(ans)



                elif 'close yourself' in query:
                    sys.exit()

                elif 'stop yourself' in query:
                    return False

                else:

                    ans = ReplyBrain(query)
                    co.ans1 = ans
                    speak(ans)

            return False
