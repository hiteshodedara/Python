import tkinter as tk
import mysql.connector

def check_login():
    # Get the username and password from the input fields
    username = username_input.get()
    password = password_input.get()

    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python"
    )
    cursor = conn.cursor()

    # Check if the username and password match a row in the database
    cursor.execute("SELECT * FROM login WHERE user=%s AND pass=%s", (username, password))
    result = cursor.fetchone()

    # If a match is found, print "Successful login"
    if result:
        print("Successful login")
    else:
        print("Incorrect username or password")

# Create a tkinter window
root = tk.Tk()

# Create a label and input field for the username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_input = tk.Entry(root)
username_input.pack()

# Create a label and input field for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_input = tk.Entry(root, show="*")
password_input.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

# Start the tkinter event loop
root.mainloop()

