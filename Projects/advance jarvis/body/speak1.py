import time

import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty(voices[2], id)
    engine.setProperty('rate', 170)
    print("")
    print(f"You: {Text}.")
    engine.say(Text)
    engine.runAndWait()


# chrome base voice
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



