#REGISTER ADMIN
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import background as background
from PIL import ImageTk
import bcrypt
import mysql.connector


# Function to establish MySQL connection
def create_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db1"
        )
        return conn
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to connect: {error}")
        return None


# Function to register a new user
def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill in the blank")
    else:
        # Check if username is already taken
        conn = create_db_connection()
        cursor = conn.cursor()

        # Hash and salt the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Insert username and hashed password into the database
        cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Registration successful.")
        root.destroy()
        import login


# Function to clear the form
def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Admin Registration")
root.geometry("760x570")
root.resizable(False, False)
root.iconbitmap('logo2.ico')
background = ImageTk.PhotoImage(file='signup2.PNG')
logo = ImageTk.PhotoImage(file='logo2.PNG')

bgLabel = Label(root, image=background)
bgLabel.grid()

signup_btn = PhotoImage(file='buttonsu.PNG')

frame = Frame(root, bg='#f4ecec')
frame.place(x=405, y=180)


# Create labels and entries for username and password
username_label = tk.Label(frame, text="Username", bg='#f4ecec', font=('Times New Roman', 14))
username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady =(5, 0))
username_entry = tk.Entry(frame,border=0, width=28, bg='#E6DFDF', fg='#4B4B4B', font=('Times New Roman', 13))

Frame(frame, width=254, height=1, bg='#666666').place(x=10, y=55)
username_entry.grid(row=1, column=0, padx=8, pady=2)

password_label = tk.Label(frame, text="Password", bg='#f4ecec', font=('Times New Roman', 14))
password_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=(8, 0))
password_entry = tk.Entry(frame,border=0, show="*", width=28, bg='#E6DFDF', fg='#4B4B4B', font=('Times New Roman', 13))
Frame(frame, width=254, height=1, bg='#666666').place(x=10, y=116)
password_entry.grid(row=4, column=0, padx=8, pady=3)

confirmation_label = tk.Label(frame, text="Confirm Password", bg='#f4ecec', font=('Times New Roman', 14))
confirmation_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=(8, 0))
confirmation_entry = tk.Entry(frame, border=0, show="*", width=28, bg='#E6DFDF', fg='#4B4B4B', font=('Times New Roman', 13))
Frame(frame, width=254, height=1, bg='#666666').place(x=10, y=178)
confirmation_entry.grid(row=6, column=0, padx=8, pady=3)


# Create buttons for registration and form clearing
signup_label = Label(frame, image=signup_btn, border=0)
signup_label.grid(row=15, column=0, columnspan=2, sticky=tk.W, padx=40, pady=(8, 0))
register_button = tk.Button(frame, text="Add ADMIN", command=register_user,  border=0,  bg='#f4ecec', font=('Times New Roman', 13,'bold'))
register_button.grid(row=15, column=0, columnspan=2, sticky=tk.W, padx=84, pady=(6, 0))



# Start the main event loop
root.mainloop()