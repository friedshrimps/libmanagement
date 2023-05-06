import mysql.connector
from tkinter import *
from tkinter import messagebox


class Livre:
    def __init__(self, id, titre, image, auteur, annee):
        self.id = id
        self.titre = titre
        self.image = image
        self.auteur = auteur
        self.annee = annee

    def delete_from_database(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db1"
        )
        c = conn.cursor()
        
        # Delete data from the "livre" table
        c.execute("DELETE FROM livres WHERE id = %s", (self.id,))

        conn.commit() # Commit the transaction
        conn.close() # Close the database connection


def delete_livre():
    # Get the ID of the livre to delete from the user
    id = id_entry.get()
    
    # Look up the livre in the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db1"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM livres WHERE id = %s", (id,))
    row = c.fetchone()
    conn.close()

    if row is None:
        messagebox.showerror("Erreur", "Livre introuvable!")
        return

    # Create a Livre object and delete it from the database
    livre = Livre(*row)
    livre.delete_from_database()

    # Clear the ID entry
    id_entry.delete(0, END)

    messagebox.showinfo("Succès", "Livre supprimé avec succès!")


root = Tk()
root.title("Supprimer un Livre")

# ID label and entry
id_label = Label(root, text="ID du Livre:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

# Delete button
delete_button = Button(root, text="Supprimer", command=delete_livre)
delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
