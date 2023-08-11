import openai
import os

fileopen = open("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\api.txt", "r")
API = fileopen.read()
fileopen.close()
openai.api_key = API


def ReplyBrain(question, chat_log=None):
    filelog = open("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\chat_log.txt", "r")
    chat_log_tamplate = filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log = chat_log_tamplate

    prompt = question
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )

    answer = response.choices[0].text.strip()
    chat_log_tamplate_update = chat_log_tamplate + \
                               f"\nYou: {question} \nReva:{answer}\n"
    filelog = open("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\chat_log.txt", "w")
    filelog.write(chat_log_tamplate_update)
    filelog.close()
    print(answer)
    return answer


def ReplyQuestion(question, chat_log=None):
    filelog = open("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\question_log.txt", "r")
    chat_log_tamplate = filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log = chat_log_tamplate

    prompt = question
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    answer = response.choices[0].text.strip()
    chat_log_tamplate_update = chat_log_tamplate + \
                               f"\nYou: {question} \nReva:{answer}"
    filelog = open("C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\question_log.txt", "w")
    filelog.write(chat_log_tamplate_update)
    filelog.close()
    print(answer)
    return answer


if __name__ == '__main__':
    pass
