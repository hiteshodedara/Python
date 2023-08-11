import tkinter as tk
from tkinter import filedialog, Text, font
import os

root = tk.Tk()

def open_file():
    file = filedialog.askopenfile(parent=root, title='Select a text file')
    if file:
        contents = file.read()
        text_area.insert('1.0', contents)
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file:
        contents = text_area.get('1.0', 'end-1c')
        file.write(contents)
        file.close()

def delete_text():
    text_area.delete('1.0', 'end')

root.title('Notepad')

# Create the main menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create the File menu
file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

# Create the Edit menu
edit_menu = tk.Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Clear', command=delete_text)

# Create the main text area
text_area = Text(root, font=('Arial', 12), undo=True)
text_area.pack(expand=True, fill='both')

# Create the Font menu
font_menu = tk.Menu(menu)
menu.add_cascade(label='Font', menu=font_menu)

# Create the Font family submenu
family_menu = tk.Menu(font_menu)
font_menu.add_cascade(label='Family', menu=family_menu)

# Create a list of font families
font_families = ['Arial', 'Courier', 'Comic Sans MS', 'Georgia', 'Verdana']

# Create a menu item for each font family
for family in font_families:
    family_menu.add_radiobutton(label=family, command=lambda f=family: text_area.config(font=(f)))

# Create the Font size submenu
size_menu = tk.Menu(font_menu)
font_menu.add_cascade(label='Size', menu=size_menu)

# Create a list of font sizes
font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

# Create a menu
for size in font_sizes:
    size_menu.add_radiobutton(label=size, command=lambda s=size: text_area.config(font=(text_area['font'][0], s)))

root.mainloop()
