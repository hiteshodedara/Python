import openai
from dotenv import load_dotenv


fileopen = open("../database/api.txt", "r")
API = fileopen.read()
fileopen.close()
openai.api_key = API
load_dotenv()
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    filelog = open("..\\database\\question_log.txt", "r")
    chat_log_tamplate = filelog.read()
    filelog.close()

    if chat_log == None:
        chat_log = chat_log_tamplate

    prompt = f'{chat_log}question:{question}\nReva : '
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0 ,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_tamplate_update = chat_log_tamplate + f"\nYou: {question} \nReva:{answer}"
    filelog = open("..\\database\\question_log.txt", "w")
    filelog.write(chat_log_tamplate_update)
    filelog.close()
    return answer


while True:
    talk = input("enter: ")
    rp = ReplyBrain(talk)
    print(rp)
