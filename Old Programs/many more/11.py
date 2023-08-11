from tkinter import *
from PIL import Image,ImageTk,ImageSequence
from time import sleep


app=Tk()
app.geometry("1000x1000")


def anime():
    global img
    
    img=Image.open("C:/Users/Hites/Desktop/Python/gg3.gif")

    l1=Label(app)
    l1.place(x=0,y=0)

    for i in ImageSequence.Iterator(img):
        
        img2=ImageTk.PhotoImage(i)
        l1.config(image=img2)
        app.update()
        sleep(0.01)
    app.after(0,anime)

Button(text="ok",command=anime).pack()

app.mainloop()