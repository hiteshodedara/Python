from tkinter import *
import random
app=Tk()


def canvas(event):
    my_list=["red","blue","black","white","purple","brown","pink","orange"]
    x,y=event.x,event.y
    c.create_line(x,x,y,y,fill=random.choice(my_list),width=10)


def left(event):
    my_list=["red","blue","black","white","purple","brown","pink","orange"]
    x,y=event.x,event.y
    c.create_rectangle(x+100,y+100,x-100,y-100,fill=random.choice(my_list))

def right(event):
    my_list=["red","blue","black","white","purple","brown","pink","orange"]
    a,b=event.x,event.y
    c.create_oval(a-b,b+a,a+b,b-a,fill=random.choice(my_list))
   
    

    
c=Canvas(app,width=500,height=500)
c.pack()
#c.bind('<Motion>',canvas)
c.bind('<Button -1>',left)
c.bind('<Button -3>',right)
app.mainloop()
