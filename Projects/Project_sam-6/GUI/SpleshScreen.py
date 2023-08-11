import tkinter
from tkinter import *
from itertools import cycle
from ttkbootstrap import Floodgauge, Label, Style
import maingui as mg

master=Tk()
master.title("Reva The Ai")
window_width = 800
window_height = 600
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_co = (screen_width / 2) - (window_width / 2)
y_co = (screen_height / 2) - (window_height / 2)
master.geometry("%dx%d+%d+%d" % (window_width, window_height, x_co, y_co))
style = Style()
style.theme_use("cosmo")



# loading animation code
def reloading_animation():
    text = cycle(["Loading", "Loading.", "Loading.", "Loading..", "Loading..", "Loading...", "Loading..."])
    label = Label(master, text="", bootstyle="primary", font=("Times New Roman", 25))
    label.place(x=350, y=190)

    def update_label():
        label.config(text=next(text))
        label.after(200, update_label)

    label.after(200, update_label)

    # second loading animation code

    text1 = cycle(["S", "St", "Sta", "Star", "Start", "Starti", "Startin",
                  "Starting", "Starting P", "Starting Pr", "Starting Pro",
                  "Starting Proj", "Starting Proje", "Starting Projec", "Starting Project",
                  "Starting Project.", "Starting Project..", "Starting Project...", ])
    label1 = Label(master, text="", bootstyle="primary", font=("Times New Roman", 25))
    label1.place(x=200, y=450)

    def update_label21():
        label1.config(text=next(text1))
        label1.after(160, update_label21)

    label1.after(250, update_label21)

    progress = Floodgauge(master, bootstyle="primary", font=("Helvetica", 18), value=0, mask="{}%",
                          orient=HORIZONTAL,
                          mode='determinate')
    progress.pack(padx=29, pady=260, fill=X)
    progress.start(30)

def hi():
    master.withdraw()
    app=Tk()
    style1 = Style()
    style1.theme_use("cosmo")
    win = mg.MainGui(app)
    win.menuframe(app)
    win.EFrame(app)
    win.chat_log(app)
    win.middleframe(app)
    app.mainloop()


reloading_animation()
master.after(3000,hi)
master.mainloop()







