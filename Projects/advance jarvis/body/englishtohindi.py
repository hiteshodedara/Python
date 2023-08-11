import tkinter as tk

root = tk.Tk()
root.title("AI Home Page")
root.geometry("600x400")

frame = tk.Frame(root, width=200, height=400)
frame.pack(side="left", fill="y")

label = tk.Label(root, text="Welcome to AI Home Page", font=("TkDefaultFont", 20), pady=20)
label.pack(fill="both", expand=True)

entry = tk.Entry(root, width=30)
entry.pack(pady=20)


def on_button_click():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")


button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

menubar = tk.Menu(frame, font=("TkDefaultFont", 60))

file_menu = tk.Menu(menubar, tearoff=0, font=("TkDefaultFont", 16))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit, font=("TkDefaultFont", 16))

help_menu = tk.Menu(menubar, tearoff=0, font=("TkDefaultFont", 16))
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", font=("TkDefaultFont", 16))

root.config(menu=menubar)
root.mainloop()
