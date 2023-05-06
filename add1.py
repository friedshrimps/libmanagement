#HOMEPAGE ADMIN
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
# Set the size of the window
root.state('zoomed')


class Livre:
    def __init__(self, id, titre, image, auteur, annee):
        self.id = id
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

        # Insert data into the "livres" table
        c.execute("INSERT INTO livres (titre, image, auteur, annee) VALUES (%s, %s, %s, %s)",
                  (self.titre, self.image, self.auteur, self.annee))

        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    @staticmethod
    def get_all_livres():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db1"
        )
        c = conn.cursor()

        # Retrieve all data from the "livres" table
        c.execute("SELECT id,titre, image, auteur, annee FROM livres")
        data = c.fetchall()

        conn.close()  # Close the database connection

        return data


def add_livre():
    root.destroy()
    import addbooks


def add_admin():
    root.destroy()
    import registeradmin


# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
# Execute the query
c = conn.cursor()
c.execute("SELECT id, titre, image, auteur, annee FROM livres")

results = c.fetchall()

root.title("Livres")
searchb = ImageTk.PhotoImage(file='searchb.PNG')
pageone = ImageTk.PhotoImage(file='pqge.PNG')

empty = Image.open('empty.PNG')
empty = empty.resize((13, 11))
emp = ImageTk.PhotoImage(empty)

searchicon = Image.open('sear.PNG')
searchicon = searchicon.resize((23, 28))
searchic = ImageTk.PhotoImage(searchicon)

dele = Image.open('dele.PNG')
dele = dele.resize((30, 30))
supp = ImageTk.PhotoImage(dele)

edit = Image.open('edit.PNG')
edit = edit.resize((30, 30))
mod = ImageTk.PhotoImage(edit)

background = ImageTk.PhotoImage(file='crubg.png')

bgLabel = Label(root, image=background)
bgLabel.pack()

frame = Frame(root, width=950, height=1960, bg='white')
frame.place(x=310, y=120)
frame.propagate(False)
# Create a list of Livre objects
livres = []
for row in results:
    id, titre, image_file, auteur, annee = row
    image = Image.open(image_file)
    # Resize the image to fit the label
    image = image.resize((120, 180), Image.Resampling.LANCZOS)
    # Convert to ImageTk object
    image_tk = ImageTk.PhotoImage(image)
    livre = Livre(id, titre, image_tk, auteur, annee)
    livres.append(livre)

# Create the card frames
cards_frame = Frame(frame, bg="white")
cards_frame.pack(pady=1, padx=2)


def search_livres():
    # Get the search query from the entry widget
    query = searchbox.get().lower()

    # Clear the existing cards
    for widget in cards_frame.winfo_children():
        widget.destroy()

    # Create new cards for the matching books
    for i, livre in enumerate(livres):
        if query in livre.titre.lower() or query in livre.auteur.lower() or query in str(livre.annee):
            card_frame = tk.Frame(cards_frame, bg='#FAF8F8', width=200, height=290, relief=tk.RAISED, border=0,
                                  highlightbackground="#BBBBBB",
                                  highlightthickness=1)
            card_frame.grid(row=i // 4, column=i % 4, padx=6, pady=(0, 10))

            card_frame.pack_propagate(False)

            # Add content to the card
            card_title = tk.Label(card_frame, text=livre.titre, bg='#FAF8F8', font=("Times New Roman", 19, 'bold'))
            card_title.pack(padx=5, pady=1)

            card_text = tk.Label(card_frame, text=livre.auteur, fg='#473B37', bg='#FAF8F8',
                                 font=("Times New Roman", 15, 'bold'))
            card_text.pack(padx=5, pady=1)

            card_text1 = tk.Label(card_frame, text=livre.id, fg='#473B37', bg='#FAF8F8',
                                  font=("Times New Roman", 15, 'bold'))
            card_text1.place(x=6, y=255)

            card_image = tk.Label(card_frame, image=livre.image)
            card_image.pack()

            # Create delete card button and delete_livre() function
            card_button = tk.Button(card_frame, bg='#FAF8F8', image=supp, border=0, activebackground='#FAF8F8',
                                    command=delete_livre)
            card_button.pack(padx=5, pady=5, side=tk.RIGHT)
            # Create edit card button and on_update_click() function
            card_button = tk.Button(card_frame, image=mod, bg='#FAF8F8', border=0, activebackground='#FAF8F8',
                                    command=lambda livre=livre: on_update_click(livre))
            card_button.pack(padx=5, pady=5, side=tk.RIGHT)

            back_button.pack_forget()

def tosp():
    root.destroy()
    import finalo

# Function to go back to the previous page
def go_back():
    # Clear the search query from the entry widget
    searchbox.delete(0, END)

    # Clear the existing cards
    for widget in cards_frame.winfo_children():
        widget.destroy()
    # Show all the books again
    search_livres()


button = Button(root, text='ADD BOOK', fg='#EFEFEF', font=('Times New Roman', 15, 'bold'), activebackground='#959595',
                activeforeground='#EFEFEF', border=0, bg='#959595', command=add_livre)
button.place(x=940, y=28)

button2 = Button(root, text='ADD ADMIN', fg='#EFEFEF', font=('Times New Roman', 15, 'bold'), activebackground='#959595',
                 activeforeground='#EFEFEF', border=0, bg='#959595', command=add_admin)
button2.place(x=1070, y=28)

p1 = Label(root, border=0, image=pageone)
p1.place(x=198, y=11)

sb = Label(root, border=0, image=searchb)
sb.place(x=530, y=21)

searchbox = Entry(root, width=25, border=0, bg='#FAF8F8', font=('Cambria', 15))
searchbox.place(x=555, y=32)

log = Button(root, text='LOGOUT', fg='#EFEFEF', font=('Times New Roman', 15, 'bold'), activebackground='#959595',
                 activeforeground='#EFEFEF', border=0, bg='#959595', command=tosp)
log.place(x=1208, y=28)

searchbutton = Button(root, border=0, bg='#D6D6D6', activebackground='#959595', image=searchic, command=search_livres)
searchbutton.place(x=892, y=31)

back_button = Button(root, bg='#FAF8F8', border=0, activebackground='#FAF8F8', image=emp, command=go_back)
back_button.place(x=860, y=40)


# Function to handle delete button click
def delete_livre():
    import delete


def on_update_click(livre):
    print(f"Updating {livre.titre}!")
    # Create a new window for the update form
    update_window = tk.Toplevel(frame)
    update_window.title(f"Modifier {livre.titre}")
    update_window.geometry("400x400")

    # Add a form for the update
    titre_label = tk.Label(update_window, text="Titre:")
    titre_label.pack()
    titre_entry = tk.Entry(update_window, width=30)
    titre_entry.pack()
    titre_entry.insert(0, livre.titre)

    auteur_label = tk.Label(update_window, text="Auteur:")
    auteur_label.pack()
    auteur_entry = tk.Entry(update_window, width=30)
    auteur_entry.pack()
    auteur_entry.insert(0, livre.auteur)

    annee_label = tk.Label(update_window, text="Année:")
    annee_label.pack()
    annee_entry = tk.Entry(update_window, width=30)
    annee_entry.pack()
    annee_entry.insert(0, livre.annee)

    # Add a button to submit the update
    def submit_update():
        # Get the updated values from the form
        updated_titre = titre_entry.get()
        updated_auteur = auteur_entry.get()
        updated_annee = annee_entry.get()

        # Update the database
        update_query = "UPDATE livres SET titre = %s, auteur = %s, annee = %s WHERE titre = %s"
        update_values = (updated_titre, updated_auteur, updated_annee, livre.titre)
        c.execute(update_query, update_values)
        conn.commit()

        # Update the Livre object with the new data
        livre.titre = updated_titre
        livre.auteur = updated_auteur
        livre.annee = updated_annee

        # Update the card with the new data
        card_title.config(text=livre.titre)
        card_text.config(text=livre.auteur)

        # Close the update window
        update_window.destroy()

    update_button = tk.Button(update_window, text="Modifier", font=("Helvetica", 14), padx=10, pady=5,
                              command=submit_update)
    update_button.pack()


# Clear the card frames and recreate them with the updated livres list
for widget in cards_frame.winfo_children():
    widget.destroy()
    widget.config(width=80)
for i, livre in enumerate(livres):
    # Add the new book to the livres list and create a new card for it
    card_frame = tk.Frame(cards_frame, bg='#FAF8F8', width=200, height=290, relief=tk.RAISED, border=0,
                          highlightbackground="#BBBBBB",
                          highlightthickness=1)
    card_frame.grid(row=i // 4, column=i % 4, padx=6, pady=(0, 10))

    card_frame.pack_propagate(False)

    # Add content to the card
    card_title = tk.Label(card_frame, text=livre.titre, bg='#FAF8F8', font=("Times New Roman", 19, 'bold'))
    card_title.pack(padx=5, pady=1)

    card_text = tk.Label(card_frame, text=livre.auteur, fg='#473B37', bg='#FAF8F8',
                         font=("Times New Roman", 15, 'bold'))
    card_text.pack(padx=5, pady=1)

    card_text1 = tk.Label(card_frame, text=livre.id, fg='#473B37', bg='#FAF8F8',
                          font=("Times New Roman", 15, 'bold'))
    card_text1.place(x=6, y=255)

    card_image = tk.Label(card_frame, image=livre.image)
    card_image.pack()

    # Create delete card button and delete_livre() function
    card_button = tk.Button(card_frame, bg='#FAF8F8', image=supp, border=0, activebackground='#FAF8F8',
                            command=delete_livre)
    card_button.pack(padx=5, pady=5, side=tk.RIGHT)
    # Create edit card button and on_update_click() function
    card_button = tk.Button(card_frame, image=mod, bg='#FAF8F8', border=0, activebackground='#FAF8F8',
                            command=lambda livre=livre: on_update_click(livre))

    card_button.pack(padx=5, pady=5, side=tk.RIGHT)

root.mainloop()