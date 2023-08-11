import tkinter as tk
from tkinter import *
from ttkbootstrap import Button, Entry, Label, Style, ScrolledText, LabelFrame, Frame
import os
import sys

from itertools import cycle
from AI.brain import ReplyBrain
from AI.speak import speak
import Reva as re


class MainGui():
    def __init__(self, master):
        self.ans2=""
        self.query=""
        master.title("Reva The Ai")
        main_window_width = 1280
        main_window_height = 720
        main_screen_width = master.winfo_screenwidth()
        main_screen_height = master.winfo_screenheight()
        main_x_co = (main_screen_width / 2) - (main_window_width / 2)
        main_y_co = (main_screen_height / 2) - (main_window_height / 2)
        master.geometry("%dx%d+%d+%d" % (main_window_width, main_window_height, main_x_co, main_y_co))
        # master.resizable(False, False)
        style = Style()
        style.theme_use("cosmo")

    def chat_log(self, master):
        def up_file():
            chat_log1.delete("1.0", END)
            file_path = "C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\chat_log.txt"

            with open(file_path, "r") as f:
                lines = f.readlines()

            lines.reverse()

            for line in lines:
                chat_log1.insert(END, line)

            master.after(3000, up_file)

        # chat log frame code
        aframe = LabelFrame(master, text=" Chat Log ", padding=5, bootstyle="warning")
        aframe.pack(side=RIGHT, padx=(5, 10), anchor=N, pady=5)
        chat_log1 = ScrolledText(aframe, width=35, height=47, font=10)
        chat_log1.pack(expand=NO)

        up_file()

    def EFrame(self, master):
        # Entry Frame Code...
        def sre():

            inpu = stext.get()
            ans = ReplyBrain(inpu)
            speak(ans)
            stext.delete(0, END)

        bframe = Frame(master)
        bframe.pack(fill=X, padx=10, pady=10, side=BOTTOM)
        stext = Entry(bframe)
        stext.pack(side=LEFT, fill=X, expand=YES, padx= 10,pady=10)
        sbutton = Button(bframe, text="SEND", bootstyle="danger-outline", command=sre)
        sbutton.pack(side=RIGHT,pady=10)

    def getrr(self,master):
        ma=MainGui(master)
        return ma.ans2,ma.query


    def menuframe(self, master):
        menuframe = Frame(master)
        menuframe.pack(pady=5, padx=10, fill=X)

        # Chat Log File
        btn_f = Button(master=menuframe, text='Chat file', compound=LEFT, command=self.open_chat_file)
        btn_f.pack(side=LEFT, anchor=N, expand=YES, ipadx=40, ipady=5, pady=5)

        # question file
        btn_b = Button(master=menuframe, text='Question file', compound=LEFT, command=self.open_question_file)
        btn_b.pack(side=LEFT, anchor=N, ipadx=40, ipady=5, expand=YES, pady=5)

        # about_us file
        btn_s = Button(master=menuframe, text='About us', compound=LEFT, command=self.open_aboutus_file)
        btn_s.pack(side=LEFT, anchor=N, expand=YES, ipadx=40, ipady=5, pady=5)

        # Contact_us file
        btn_se = Button(master=menuframe, text='Contact us', compound=LEFT, command=self.open_contactus_file)
        btn_se.pack(side=LEFT, anchor=N, expand=YES, ipadx=40, ipady=5, pady=5)

        # close
        btn_c = Button(master=menuframe, text='Close', compound=LEFT, command=sys.exit)
        btn_c.pack(side=LEFT, anchor=N, expand=YES, ipadx=40, ipady=5, pady=5)

    def middleframe(self, master):
        # main Frame
        f_main = Frame(master, bootstyle="dark")
        f_main.pack(fill=BOTH, ipady=220)

        # Down Part of a Main Frame
        down_f = Frame(f_main, bootstyle="dark")
        down_f.pack(fill=BOTH, side=BOTTOM, pady=30)

        com = re.Commands()

        def comm():
            while True:
                com.command()

        st_btn = tk.Button(down_f, text="Start", width=10, font=("Helvetica", 15), command=comm)
        st_btn.pack(side=BOTTOM)

        # Middle Frame of main Frame
        lr_frame = Frame(f_main, bootstyle="dark")
        lr_frame.pack(fill=BOTH, side=TOP)

        # ok1=re.Commands()
        # r=ok1.geter()
        text = cycle(["Working", "Working.", "Working.", "Working..", "Working..", "Working...", "Working..."])


        def update_label3():
            lr_label.config(text=next(text))
            lr_label.after(200, update_label3)



        lr_label = Label(lr_frame, text="", bootstyle="danger", font=("Helvetica", 30))
        lr_label.pack(pady=(200, 0))
        lr_label.after(200, update_label3)
        # Label Frame of Main Frame
        lb_frame = Frame(f_main, bootstyle="dark")
        lb_frame.pack(fill=BOTH, side=BOTTOM, padx=(30, 10))

        ma = MainGui(master)
        a,q=ma.getrr(master)



    # def open_file1(self):
    #     win.open_file(app)

    def open_chat_file(self, file=None):
        tk1 = tk.Tk()

        top = tk.Toplevel(tk1)
        top.title("Chat Log File")
        text = tk.Text(top, width=65, height=20, font="consolas 14")
        text.pack()
        path = "C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\chat_log.txt"
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file:
                content_in_file = file.read()
            text.delete('1.0', tk.END)
            text.insert('1.0', content_in_file)
            text.config(stat=DISABLED)
        tk1.withdraw()

    def open_question_file(self, file=None):
        tk1 = tk.Tk()
        top = tk.Toplevel(tk1)
        top.title("Question Log File")
        text = tk.Text(top, width=65, height=20, font="consolas 14")
        text.pack()
        path = "C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\question_log.txt"
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file:
                content_in_file = file.read()
            text.delete('1.0', tk.END)
            text.insert('1.0', content_in_file)
            text.config(stat=DISABLED)
        tk1.withdraw()

    def open_aboutus_file(self, file=None):
        tk1 = tk.Tk()
        top = tk.Toplevel(tk1)
        top.title("About us File")
        text = tk.Text(top, width=70, height=20, font="consolas 14")
        text.pack()
        path = "C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\about_us.txt"
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file:
                content_in_file = file.read()
            text.delete('1.0', tk.END)
            text.insert('1.0', content_in_file)
            text.config(stat=DISABLED)
        tk1.withdraw()

    def open_contactus_file(self, file=None):
        tk1 = tk.Tk()
        top = tk.Toplevel(tk1)
        top.title("Contact us File")
        text = tk.Text(top, width=70, height=20, font="consolas 14")
        text.pack()
        path = "C:\\Users\\Hites\\Documents\\Project_sam-6\\database\\contact_us.txt"
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file:
                content_in_file = file.read()
            text.delete('1.0', tk.END)
            text.insert('1.0', content_in_file)
            text.config(stat=DISABLED)
        tk1.withdraw()

    def tok(self, app):
        win = MainGui(app)
        win.menuframe(app)
        win.EFrame(app)
        win.chat_log(app)
        win.middleframe(app)
        app.mainloop()




if __name__ == '__main__':
    app = Tk()
    mg=MainGui(app)
    mg.tok(app)





