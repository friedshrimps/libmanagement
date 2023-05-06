#LOGIN
import bcrypt
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def get_db_connection():
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


def login_user():
    username = username_entry.get()
    passw = password_entry.get()
    adm = ad.get()

    hashpassword = passw.encode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    if adm == 1:
        cursor.execute("SELECT password FROM admin WHERE username = %s", (username,))
        row = cursor.fetchone()
        if not row:
            messagebox.showerror("Error", "Incorrect Data")
            conn.close()

        password = row[0].encode('ascii')

        if bcrypt.checkpw(hashpassword, password):
            cursor.close()

            # messagebox.showinfo("Success", "Login successful.")
            root.destroy()
            import add1

        else:
            messagebox.showerror("Error", "Login Failed!")
            conn.close()

    else:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()

        if not row:
            messagebox.showerror("Error", "Incorrect Data")
            conn.close()

        password = row[0].encode('ascii')

        if bcrypt.checkpw(hashpassword, password):
            cursor.close()

            # messagebox.showinfo("Success", "Login successful.")
            root.destroy()
            import home

        else:
            messagebox.showerror("Error", "Login Failed!")
            conn.close()

def return_s():
    root.destroy()
    import finalsu

root = tk.Tk()
root.title("Login ")
root.geometry("760x570")
root.resizable(False, False)
root.iconbitmap('logo2.ico')
background = ImageTk.PhotoImage(file='login2.png')

arro =ImageTk.PhotoImage(file='arro.PNG')

login_btn =ImageTk.PhotoImage(file='capture1.png')

bgLabel = Label(root, image=background)
bgLabel.grid()

username_entry = tk.Entry(root, bg='#6A5953', font=('Times New Roman', 12), fg='white', width=30, border=0)
username_entry.place(x=358, y=207)

password_entry = tk.Entry(root, show="*", bg='#6A5953', font=('Times New Roman', 12), fg='white', width=30, border=0)
password_entry.place(x=358, y=269)

ad = BooleanVar()
admin = Checkbutton(root, bg='#6A5953', activebackground='#6A5953', variable=ad)
admin.place(x=352, y=299)

asadmin = Label(root, bg='#6A5953', fg='#F4ECEC', text='Admin', font=('Times New Roman', 12, 'bold'))
asadmin.place(x=375, y=299)

forgot_button = tk.Button(root, text="Forgot Password?", bg='#6A5953', font=('Times New Roman', 11, 'bold'),
                          activebackground='#6A5953', activeforeground='white', border=0, fg='#F4ECEC',
                          command=login_user)
forgot_button.place(x=555, y=299)

login_label = Label(root, image=login_btn, border=0)
login_label.place(x=378, y=334)

ret_button = Button(root, image=arro, activebackground='#F4ECEC', bg='#F4ECEC', border=0, command=return_s)
ret_button.place(x=298, y=356)

login_button = tk.Button(root, text="LOGIN", fg='#F4ECEC', bg='#6A5953', activebackground='#6A5953', activeforeground='#F4ECEC', command=login_user, border=0,
                         font=('Times New Roman', 13, 'bold'))
login_button.place(x=478, y=341)

root.mainloop()
