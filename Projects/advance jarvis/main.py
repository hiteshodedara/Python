import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from googletrans import Translator
import speech_recognition as sr

fileopen = open("database/api.txt", "r")
API = fileopen.read()
fileopen.close()
openai.api_key = API
load_dotenv()
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    filelog = open("database/chat_log.txt", "r")
    chat_log_tamplate = filelog.read()
    filelog.close()

    if chat_log == None:
        chat_log = chat_log_tamplate

    prompt = f'{chat_log}You:{question}\nReva : '
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_tamplate_update = chat_log_tamplate + f"\nYou: {question} \nReva:{answer}"
    filelog = open("database/chat_log.txt", "w")
    filelog.write(chat_log_tamplate_update)
    filelog.close()
    return answer


# speak Function for a ai

chrome_op = Options()
chrome_op.add_argument('--log-level=3')
chrome_op.headless = True
path = 'database//chromedriver.exe'
driver = webdriver.Chrome(path, options=chrome_op)
driver.maximize_window()
website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('Indian English / Raveena')


def speak(text):
    lengthftext = len(str(text))
    if lengthftext == 0:
        pass
    else:
        print("")
        print(f"Ai: {text}.")
        print("")
        data = str(text)
        xpath = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpath).send_keys(data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthftext >= 30:
            sleep(4)

        elif lengthftext >= 40:
            sleep(6)

        elif lengthftext >= 55:
            sleep(8)

        elif lengthftext >= 70:
            sleep(10)

        elif lengthftext >= 100:
            sleep(12)

        elif lengthftext >= 110:
            sleep(14)

        else:
            sleep(2)


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")

    except:
        return ""

    query = str(query).lower()
    return query


def TranslaterText(Text):
    line = str(Text)
    translates = Translator()
    result = translates.translate(line)
    data = result.text
    print(f"You: {data}.")
    return data


def MicExecution():
    query = Listen()
    data = TranslaterText(query)
    return data


query = MicExecution()
ans = ReplyBrain(query)
speak(ans)
