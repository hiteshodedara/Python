#import requests

#timeout=1
#try:
#   requests.head("http://www.google.com",timeout=timeout)
#   print("ok")
#except requests.ConnectionError:
#    print("no")
import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("My App")

# Open the GIF file
image = Image.open("0001.gif")

# Create a PhotoImage object to display the GIF
photo_image = ImageTk.PhotoImage(image)

# Create a label widget and set the image as its background
label = tk.Label(image=photo_image)
label.pack()

# Run the main loop
window.mainloop()
