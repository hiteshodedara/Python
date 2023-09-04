from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
import webbrowser
from bs4 import BeautifulSoup
import requests
import os
import openai

fileopen = open("/home/hiteshodii/PycharmProjects/pythonProject1/api_key.txt")
API = fileopen.read()
fileopen.close()
openai.api_key = API
print(API)


# Function to open a YouTube video
def open_youtube_video():
    webbrowser.open("https://www.youtube.com/playlist?list=PLd3UqWTnYXOmx_J1774ukG_rvrpyWczm0")


# Function to open another YouTube video
def open_another_video():
    webbrowser.open("https://www.youtube.com/watch?v=ANOTHER_VIDEO_ID")


# chatgpt function

def send_message():
    user_input = user_input_text.get("1.0", "end-1c")  # Get user input
    chat_history = chat_history_text.get("1.0", "end-1c")  # Get chat history

    # Send user input and get a response from GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50,  # Adjust this value as needed
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    bot_response = response.choices[0].text
    chat_history += f"\nYou: {user_input}\nBot: {bot_response}"

    # Update the chat history text
    chat_history_text.delete("1.0", "end")
    chat_history_text.insert("end", chat_history)


# Function to display the latest news from India
def get_latest_news():
    # Scraping news from a website (replace with your preferred news source)
    url = "https://www.aajtak.in/india/gujarat"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and display the news headlines
    headlines = [headline.text for headline in soup.find_all("h2")]
    news_text = "\n\n".join(headlines)

    # Create a new window to display the news
    news_window = Toplevel(root)
    news_window.title("Latest News from India")
    news_label = Label(news_window, text=news_text, font=("Helvetica", 12, "bold"), justify=tk.LEFT)
    news_label.pack()
    read_btn = tk.Button(news_window, text="read", width=10, background="white")
    read_btn.pack()


# Create the main application window
root = Tk()
root.title("Main Application")
root.geometry("800x600")

# Load icons as images using Pillow
youtube_icon = PhotoImage(file="icons8-youtube-96.png")  # Replace with your icon image file

news_icon = PhotoImage(file="icons8-news-94.png")  # Replace with your icon image file

chatgpt_icon = PhotoImage(file="icons8-chatgpt-96.png")  # Replace with your icon image file

# Create a big title label with styling
title_label = Label(root, text="Main Application", font=("Helvetica", 24, "bold"), foreground="orange")
title_label.pack(pady=20)

# Create a frame for buttons
button_frame = tk.Frame(root, background="white")
button_frame.pack(pady=20, side=LEFT)

# Create icon buttons using PhotoImage and set the compound option to 'left'
button1 = tk.Button(button_frame, image=youtube_icon, borderwidth=0, background="white", highlightthickness=0,
                    command=open_youtube_video)
button2 = tk.Button(button_frame, image=youtube_icon, borderwidth=0, background="white", highlightthickness=0,
                    command=open_another_video)
button3 = tk.Button(button_frame, image=news_icon, borderwidth=0, background="white", highlightthickness=0,
                    command=get_latest_news)

lb1 = tk.Button(button_frame, text="Durga Sir Playlist", font=("Helvetica", 18, "bold"), borderwidth=0,
                background="white", highlightthickness=0, command=open_youtube_video)
lb2 = tk.Button(button_frame, text="Other video", font=("Helvetica", 18, "bold"), borderwidth=0, background="white",
                highlightthickness=0, command=open_youtube_video)
lb3 = tk.Button(button_frame, text="Gujarat latest News", font=("Helvetica", 18, "bold"), borderwidth=0,
                background="white", highlightthickness=0, command=get_latest_news)

button1.grid(row=0, pady=(20, 20), padx=10)
lb1.grid(row=0, column=1, pady=10, padx=10)

button2.grid(row=2, pady=10, padx=10)
lb2.grid(row=2, column=1, pady=10, sticky=W, padx=10)

button3.grid(row=3, column=0, pady=2)
lb3.grid(row=3, column=1, pady=10, padx=10)

gpt_frame = tk.Frame(root, background="white")
gpt_frame.pack(pady=20, side=RIGHT)

chat_history_text = scrolledtext.ScrolledText(gpt_frame, wrap=tk.WORD, width=50, height=20)
chat_history_text.grid(row=1, column=0)

# Create an entry widget for user input
user_input_text = tk.Text(gpt_frame, wrap=tk.WORD, width=50, height=2)
user_input_text.grid(row=2, column=0)

# Create a button to send the user's message
send_button = tk.Button(gpt_frame, text="Send", command=send_message)
send_button.grid(row=3, column=0)
# Run the Tkinter event loop
root.mainloop()
