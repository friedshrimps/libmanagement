import mysql.connector
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class Livre:
    def __init__(self, titre, image, auteur, annee):
        self.titre = titre
        self.image = image
        self.auteur = auteur
        self.annee = annee

    def insert_into_database(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db1"
        )
        c = conn.cursor()

        # Insert data into the "livre" table
        c.execute("INSERT INTO livres (titre, image, auteur, annee) VALUES (%s, %s, %s, %s)",
                  (self.titre, self.image, self.auteur, self.annee))

        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.image = file_path
        self.image_label.config(text=file_path)


def submit_form():
    titre = titre_entry.get()
    image = livre.image
    auteur = auteur_entry.get()
    annee = annee_entry.get()

    livre_obj = Livre(titre, image, auteur, annee)
    livre_obj.insert_into_database()

    # Clear form entries and image label
    titre_entry.delete(0, END)
    auteur_entry.delete(0, END)
    annee_entry.delete(0, END)
    livre.image = None
    livre.image_label.config(text="")

    print("Data inserted successfully!")


root = Tk()
root.title("Livre Form")
root.geometry('590x396')
background = ImageTk.PhotoImage(file='addbk.PNG')

bgLabel = Label(root, image=background)
bgLabel.grid()

addic = Image.open('addic.PNG')
addic = addic.resize((60, 50))
add = ImageTk.PhotoImage(addic)

browseic = Image.open('browse1.PNG')
browseic = browseic.resize((52, 48))
browse = ImageTk.PhotoImage(browseic)

image_label = Label(root, bg='#C0B7B3', font=('Times New Roman', 12, 'bold'), fg='#675650', width=28, border=0)
image_label.place(x=261, y=255)

# Form entries
titre_entry = Entry(root, bg='#C0B7B3', font=('Times New Roman', 14, 'bold'), fg='#675650', width=30, border=0)
titre_entry.place(x=186, y=65)
auteur_entry = Entry(root, bg='#C0B7B3', font=('Times New Roman', 14, 'bold'), fg='#675650', width=30, border=0)
auteur_entry.place(x=186, y=124)
annee_entry = Entry(root, bg='#C0B7B3', font=('Times New Roman', 14, 'bold'), fg='#675650', width=30, border=0)
annee_entry.place(x=186, y=191)

livre = Livre(None, None, None, None)
livre.image_label = image_label

# Browse image button
browse_button = Button(root, image=browse, bg='#C0B7B3', activebackground='#C0B7B3', border=0,
                       command=livre.browse_image)
browse_button.place(x=196, y=242)

# Submit button
submit_button = Button(root, image=add, activebackground='#675650', bg='#675650', border=0, command=submit_form)
submit_button.place(x=131, y=301)

root.mainloop()
