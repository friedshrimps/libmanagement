#HOMEPAGE USER
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
# Set the size of the window
root.state('zoomed')

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
        c.execute("SELECT titre, image, auteur, annee FROM livres")
        data = c.fetchall()

        conn.close()  # Close the database connection

        return data



# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
# Execute the query
c = conn.cursor()
c.execute("SELECT titre, image, auteur, annee FROM livres")

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

cart = Image.open('cartb.PNG')
cart = cart.resize((30, 30))
cartb = ImageTk.PhotoImage(cart)

edit = Image.open('edit.PNG')
edit = edit.resize((30, 30))
mod = ImageTk.PhotoImage(edit)

background = ImageTk.PhotoImage(file='crubg.png')

bgLabel = Label(root, image=background)
bgLabel.pack()

frame = Frame(root, width=950, height=1960, bg='white')
frame.place(x=310, y=180)
frame.propagate(False)
# Create a list of Livre objects
livres = []
for row in results:
    titre, image_file, auteur, annee = row
    image = Image.open(image_file)
    # Resize the image to fit the label
    image = image.resize((120, 180), Image.Resampling.LANCZOS)
    # Convert to ImageTk object
    image_tk = ImageTk.PhotoImage(image)
    livre = Livre(titre, image_tk, auteur, annee)
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
            card_frame = tk.Frame(cards_frame, bg='#FAF8F8', relief=tk.RAISED, border=0, highlightbackground="#BBBBBB",
                                  highlightthickness=1)
            card_frame.grid(row=i // 5, column=i % 5, ipadx=16, padx=6, pady=(0, 10))

            # Add content to the card
            card_title = tk.Label(card_frame, text=livre.titre, bg='#FAF8F8', font=("Times New Roman", 19, 'bold'))
            card_title.pack(padx=5, pady=3)

            card_text = tk.Label(card_frame, text=livre.auteur, fg='#473B37', bg='#FAF8F8',
                                 font=("Times New Roman", 15, 'bold'))
            card_text.pack(padx=5, pady=5)

            card_text1 = tk.Label(card_frame, text=livre.annee, fg='#473B37', bg='#FAF8F8',
                                  font=("Times New Roman", 15, 'bold'))
            card_text1.place(x=6, y=259)

            card_image = tk.Label(card_frame, image=livre.image)
            card_image.pack()

            # Create delete card button and delete_livre() function
            card_button = tk.Button(card_frame, bg='#FAF8F8', image=cartb, border=0, activebackground='#FAF8F8' )
            card_button.pack(padx=5, pady=5, side=tk.RIGHT)


            back_button.pack_forget()


# Function to go back to the previous page
def go_back():
    # Clear the search query from the entry widget
    searchbox.delete(0, END)

    # Clear the existing cards
    for widget in cards_frame.winfo_children():
        widget.destroy()
    # Show all the books again
    search_livres()

def tosp():
    root.destroy()
    import finalo



p1 = Label(root, border=0, image=pageone)
p1.place(x=198, y=11)

sb = Label(root, border=0, image=searchb)
sb.place(x=580, y=21)


searchbox = Entry(root, width=25, border=0, bg='#FAF8F8', font=('Cambria', 15))
searchbox.place(x=605, y=33)

log = Button(root, text='LOGOUT', fg='#EFEFEF', font=('Times New Roman', 15, 'bold'), activebackground='#959595',
                 activeforeground='#EFEFEF', border=0, bg='#959595', command=tosp)
log.place(x=1205, y=28)


searchbutton = Button(root, border=0, bg='#D6D6D6', activebackground='#959595', image=searchic, command=search_livres)
searchbutton.place(x=942, y=31)

back_button = Button(root, bg='#FAF8F8', border=0, activebackground='#FAF8F8', image=emp, command=go_back)
back_button.place(x=910, y=40)



for i, livre in enumerate(livres):
    # Add the new book to the livres list and create a new card for it
    card_frame = tk.Frame(cards_frame, bg='#FAF8F8', width=200, height=290, relief=tk.RAISED, border=0, highlightbackground="#BBBBBB",
                          highlightthickness=1)
    card_frame.grid(row=i // 4, column=i % 4,  padx=6, pady=(0, 10))

    card_frame.pack_propagate(False)

    # Add content to the card
    card_title = tk.Label(card_frame, text=livre.titre, bg='#FAF8F8', font=("Times New Roman", 19, 'bold'))
    card_title.pack(padx=5, pady=1)

    card_text = tk.Label(card_frame, text=livre.auteur, fg='#473B37', bg='#FAF8F8',
                         font=("Times New Roman", 15, 'bold'))
    card_text.pack(padx=5, pady=1)

    card_text1 = tk.Label(card_frame, text=livre.annee, fg='#473B37', bg='#FAF8F8',
                          font=("Times New Roman", 15, 'bold'))
    card_text1.place(x=6, y=255)

    card_image = tk.Label(card_frame, image=livre.image)
    card_image.pack()

    # Create delete card button and delete_livre() function
    card_button = tk.Button(card_frame, bg='#FAF8F8', image=cartb, border=0, activebackground='#FAF8F8',
                          )
    card_button.pack(padx=5, pady=5, side=tk.RIGHT)


root.mainloop()
