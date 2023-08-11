from tkinter import *
from PIL import Image

app=Tk()
gifimage="gg.gif"

openimage=Image.open(gifimage)
frames=openimage.n_frames

imageobj=[PhotoImage(file=gifimage,format=f"gif -index {i}") for i in range(frames)]

count=0
showanimation=None

def animation(count):
    global showanimation
    newImage=imageobj[count]

    gif_label.configure(image=newImage)
    count +=1
    if count == frames:
        count=0
    showanimation=app.after(50,lambda: animation(count))


gif_label=Label(app,image="")
gif_label.pack()

animation(count)


app.mainloop()
