#SIGNUP USER
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import bcrypt
import mysql.connector

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

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
def logeuin():
    root.destroy()
    import finalo
# Function to register a new user
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    confirmation = confirmation_entry.get()
    tc = termvar.get()
    if username == "" or password == "" or confirmation == ""  or tc == 0:
        messagebox.showerror("Error", "Please fill in all fields.")
    elif password != confirmation:
        messagebox.showerror("Error", "Passwords do not match.")
    else:
        # Check if username is already taken
        conn = create_db_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone() is not None:
            messagebox.showerror("Error", "Username already taken.")
        else:
            # Hash and salt the password
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Insert username and hashed password into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()

            # Create a new User object and store it in a file
            user = User(None, username, hashed_password)
            with open("users.txt", "a") as file:
                file.write(f"{user.id},{user.username},{user.password}\n")

            messagebox.showinfo("Success", "Registration successful.")
            root.destroy()
            import home

# Function to clear the form
def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirmation_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("760x570")
root.resizable(False, False)
root.iconbitmap('logo2.ico')

background = ImageTk.PhotoImage(file='signup2.PNG')
logo = ImageTk.PhotoImage(file='logo2.PNG')

bgLabel = Label(root, image=background)
bgLabel.grid()

signup_btn = PhotoImage(file='buttonsu.PNG')

frame = Frame(root, bg='#f4ecec')
frame.place(x=405, y=155)

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

termvar = BooleanVar()

terms = Checkbutton(frame, bg='#f4ecec', fg='#666666', activebackground='#f4ecec', activeforeground='#666666',
                    text='I agree to all the Terms and Conditions', font=('Times New Roman', 12), variable=termvar)
terms.grid(row=7, column=0, sticky=tk.W, padx=5, pady=(6, 0))

# Create buttons for registration and form clearing
signup_label = Label(frame, image=signup_btn)
signup_label.grid(row=8, column=0, columnspan=2, sticky=tk.W, padx=40, pady=(8, 0))
register_button = tk.Button(frame, text="SIGN UP", command=register_user,  border=0,  bg='#f4ecec', font=('Times New Roman', 13))
register_button.grid(row=8, column=0, columnspan=2, sticky=tk.W, padx=99, pady=(6, 0))


haveaccount = tk.Label(frame, bg='#f4ecec', fg='#666666', text='Already have an account?', font=('Times New Roman', 12))
haveaccount.grid(row=9, column=0, sticky=tk.W, padx=31, pady=(2, 0))

loginnew = Button(frame, text='Log in', border=0, font=('Times New Roman',11,'bold underline'), command=logeuin, cursor='hand2', fg='#675650', bg='#f4ecec')
loginnew.place(x=189, y=277)

# Start the main event loop
root.mainloop()