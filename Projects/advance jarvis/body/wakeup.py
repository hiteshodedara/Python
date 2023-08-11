import speech_recognition as sr
import os


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:

        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query


def wakeup():
    querys = Listen().lower()

    if 'wake up' in querys:
        os.startfile(r'C:\Users\Hites\Documents\advance jarvis\main.py')

    else:
        pass


while True:
    wakeup()
