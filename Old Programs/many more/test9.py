import tkinter as tk
from tkinter import Label
from itertools import cycle

def reloading_animation():
    text = cycle(["Loading.", "Loading..", "Loading..."])
    def update_label():
        label.config(text=next(text))
        label.after(200, update_label)

    root = tk.Tk()
    label = Label(root, text="Loading.")
    label.pack()
    label.after(200, update_label)
    root.mainloop()

reloading_animation()
