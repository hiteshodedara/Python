import tkinter as tk

def spin():
    global icon
    icon = (icon + 1) % 8
    label.config(image=images[icon])
    root.after(100, spin)

root = tk.Tk()
images = [tk.PhotoImage(file='images.png'.format(i)) for i in range(8)]
icon = 0
label = tk.Label(root, image=images[icon])
label.pack()

spin()
root.mainloop()
