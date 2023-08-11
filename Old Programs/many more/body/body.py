from tkinter import *


app=Tk()
app.title("Reva")
app.geometry("400x300")

    
def body():
    l1.config(text="bhuro")
    bl1=l1.cget("text")
    return bl1


l1=Label(text="")
l1.pack()





