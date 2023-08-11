from tkinter import *



def left(event):
    global a
    a=event.x
    global b
    b=event.y

def motion(event):
    x,y=event.x,event.y
    c.create_rectangle(a,b,x,y,fill="red")
    c.delete('all')
    
def rel(event):
    x,y=event.x,event.y
    c.create_rectangle(a,b,x,y,fill="red")







app = Tk()
app.geometry("700x700")
app.configure(background="red")
c=Canvas(width=500,height=500)
c.pack(padx=100,pady=100)

c.bind('<Button -1>',left)
c.bind('B1-Motion',motion)
c.bind('<ButtonRelease>',rel)




app.mainloop()
