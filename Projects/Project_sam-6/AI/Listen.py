import speech_recognition as sr
import tkinter as tk
import GUI.maingui as mg



class listen():



    def Listen(self):

        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 8)

        try:

            print("Recognizing...")

            query = r.recognize_google(audio)

        except:
            return None

        return query



if __name__ == '__main__':
    la = listen()
