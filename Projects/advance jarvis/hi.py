from tkinter import *

app=Tk()
app.title("splase screen..")
l1=Label(app,text="splese screen")
l1.pack()

def main():

    app.destroy()
    root=Tk()
    l1=Label(root,text="main screen")
    l1.pack()

app.after(3000,main)
mainloop()
