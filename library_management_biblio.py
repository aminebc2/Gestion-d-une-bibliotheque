import tkinter as tk
from tkinter import ttk
import sqlite3

# Function to add a book
def ajouter_livre():
    # Get the input values from the form
    titre = titre_entry.get()
    auteur = auteur_entry.get()
    editeur = editeur_entry.get()
    date_publication = date_publication_entry.get()
    categorie = categorie_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Insert the book into the database
    cursor.execute("INSERT INTO livres (titre, auteur, editeur, date_publication, categorie) VALUES (?, ?, ?, ?, ?)",
                   (titre, auteur, editeur, date_publication, categorie))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form fields
    titre_entry.delete(0, tk.END)
    auteur_entry.delete(0, tk.END)
    editeur_entry.delete(0, tk.END)
    date_publication_entry.delete(0, tk.END)
    categorie_entry.delete(0, tk.END)

    # Perform any other actions after adding the book
    print("Book added successfully.")

# Function to modify a book
def modifier_livre():
    # Get the input values from the form
    livre_id = livre_id_entry.get()
    status = status_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Update the book status in the database
    cursor.execute("UPDATE livres SET status=? WHERE id=?", (status, livre_id))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form fields
    livre_id_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

    # Perform any other actions after modifying the book
    print("Book modified successfully.")

# Function to remove a book
def supprimer_livre():
    # Get the input value from the form
    livre_id = livre_id_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Delete the book from the database
    cursor.execute("DELETE FROM livres WHERE id=?", (livre_id,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form field
    livre_id_entry.delete(0, tk.END)

    # Perform any other actions after removing the book
    print("Book removed successfully.")

# Function to confirm a reservation
def confirmer_reservation():
    # Get the input value from the form
    reservation_id = reservation_id_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Update the reservation status to Confirmed
    cursor.execute("UPDATE reservations SET status='Confirmed' WHERE id=?", (reservation_id,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form field
    reservation_id_entry.delete(0, tk.END)

    # Perform any other actions after confirming the reservation
    print("Reservation confirmed successfully.")

# Function to remove a reservation
def supprimer_reservation():
    # Get the input value from the form
    reservation_id = reservation_id_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Delete the reservation from the database
    cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form field
    reservation_id_entry.delete(0, tk.END)

    # Perform any other actions after removing the reservation
    print("Reservation removed successfully.")

# Function to create a loan
def creer_pret():
    # Get the input values from the form
    date_debut = date_debut_entry.get()
    date_fin = date_fin_entry.get()
    id_adherant = id_adherant_entry.get()
    id_livre = id_livre_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Insert the loan into the database
    cursor.execute("INSERT INTO pret (date_debut, date_fin, id_user, id_livre) VALUES (?, ?, ?, ?)",
                   (date_debut, date_fin, id_adherant, id_livre))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form fields
    date_debut_entry.delete(0, tk.END)
    date_fin_entry.delete(0, tk.END)
    id_adherant_entry.delete(0, tk.END)
    id_livre_entry.delete(0, tk.END)

    # Perform any other actions after creating the loan
    print("Loan created successfully.")

# Function to remove a loan
def supprimer_pret():
    # Get the input value from the form
    pret_id = pret_id_entry.get()

    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Delete the loan from the database
    cursor.execute("DELETE FROM prets WHERE id=?", (pret_id,))
    conn.commit()

    # Close the database connection
    conn.close()

    # Clear the form field
    pret_id_entry.delete(0, tk.END)

    # Perform any other actions after removing the loan
    print("Loan removed successfully.")

# Create the main window
window = tk.Tk()
window.title("Library Management")

# Create the Tabbed Pane widget
tabbed_pane = ttk.Notebook(window)

# Create the "Ajouter Livre" tab
ajouter_livre_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Ajouter Livre" tab
titre_label = tk.Label(ajouter_livre_tab, text="Titre:")
titre_label.pack()

titre_entry = tk.Entry(ajouter_livre_tab)
titre_entry.pack()

auteur_label = tk.Label(ajouter_livre_tab, text="Auteur:")
auteur_label.pack()

auteur_entry = tk.Entry(ajouter_livre_tab)
auteur_entry.pack()

editeur_label = tk.Label(ajouter_livre_tab, text="Editeur:")
editeur_label.pack()

editeur_entry = tk.Entry(ajouter_livre_tab)
editeur_entry.pack()

date_publication_label = tk.Label(ajouter_livre_tab, text="Date de publication:")
date_publication_label.pack()

date_publication_entry = tk.Entry(ajouter_livre_tab)
date_publication_entry.pack()

categorie_label = tk.Label(ajouter_livre_tab, text="Catégorie:")
categorie_label.pack()

categorie_entry = tk.Entry(ajouter_livre_tab)
categorie_entry.pack()

ajouter_livre_button = tk.Button(ajouter_livre_tab, text="Ajouter Livre", command=ajouter_livre)
ajouter_livre_button.pack()

# Add the "Ajouter Livre" tab to the Tabbed Pane
tabbed_pane.add(ajouter_livre_tab, text="Ajouter Livre")

# Create the "Modifier Livre" tab
modifier_livre_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Modifier Livre" tab
livre_id_label = tk.Label(modifier_livre_tab, text="ID du Livre:")
livre_id_label.pack()

livre_id_entry = tk.Entry(modifier_livre_tab)
livre_id_entry.pack()

status_label = tk.Label(modifier_livre_tab, text="Status:")
status_label.pack()

status_entry = tk.Entry(modifier_livre_tab)
status_entry.pack()

modifier_livre_button = tk.Button(modifier_livre_tab, text="Modifier Livre", command=modifier_livre)
modifier_livre_button.pack()

# Add the "Modifier Livre" tab to the Tabbed Pane
tabbed_pane.add(modifier_livre_tab, text="Modifier Livre")

# Create the "Supprimer Livre" tab
supprimer_livre_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Supprimer Livre" tab
livre_id_label = tk.Label(supprimer_livre_tab, text="ID du Livre:")
livre_id_label.pack()

livre_id_entry = tk.Entry(supprimer_livre_tab)
livre_id_entry.pack()

supprimer_livre_button = tk.Button(supprimer_livre_tab, text="Supprimer Livre", command=supprimer_livre)
supprimer_livre_button.pack()

# Add the "Supprimer Livre" tab to the Tabbed Pane
tabbed_pane.add(supprimer_livre_tab, text="Supprimer Livre")

# Create the "Confirmer Reservation" tab
confirmer_reservation_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Confirmer Reservation" tab
reservation_id_label = tk.Label(confirmer_reservation_tab, text="ID de la Reservation:")
reservation_id_label.pack()

reservation_id_entry = tk.Entry(confirmer_reservation_tab)
reservation_id_entry.pack()

confirmer_reservation_button = tk.Button(confirmer_reservation_tab, text="Confirmer Reservation", command=confirmer_reservation)
confirmer_reservation_button.pack()

# Add the "Confirmer Reservation" tab to the Tabbed Pane
tabbed_pane.add(confirmer_reservation_tab, text="Confirmer Reservation")

# Create the "Supprimer Reservation" tab
supprimer_reservation_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Supprimer Reservation" tab
reservation_id_label = tk.Label(supprimer_reservation_tab, text="ID de la Reservation:")
reservation_id_label.pack()

reservation_id_entry = tk.Entry(supprimer_reservation_tab)
reservation_id_entry.pack()

supprimer_reservation_button = tk.Button(supprimer_reservation_tab, text="Supprimer Reservation", command=supprimer_reservation)
supprimer_reservation_button.pack()

# Add the "Supprimer Reservation" tab to the Tabbed Pane
tabbed_pane.add(supprimer_reservation_tab, text="Supprimer Reservation")

# Create the "Créer Pret" tab
creer_pret_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Créer Pret" tab
date_debut_label = tk.Label(creer_pret_tab, text="Date de début:")
date_debut_label.pack()

date_debut_entry = tk.Entry(creer_pret_tab)
date_debut_entry.pack()

date_fin_label = tk.Label(creer_pret_tab, text="Date de fin:")
date_fin_label.pack()

date_fin_entry = tk.Entry(creer_pret_tab)
date_fin_entry.pack()

id_adherant_label = tk.Label(creer_pret_tab, text="ID de l'Adhérent:")
id_adherant_label.pack()

id_adherant_entry = tk.Entry(creer_pret_tab)
id_adherant_entry.pack()

id_livre_label = tk.Label(creer_pret_tab, text="ID du Livre:")
id_livre_label.pack()

id_livre_entry = tk.Entry(creer_pret_tab)
id_livre_entry.pack()

creer_pret_button = tk.Button(creer_pret_tab, text="Créer Prêt", command=creer_pret)
creer_pret_button.pack()

# Add the "Créer Pret" tab to the Tabbed Pane
tabbed_pane.add(creer_pret_tab, text="Créer Pret")

# Create the "Supprimer Pret" tab
supprimer_pret_tab = ttk.Frame(tabbed_pane)

# Create and position elements in the "Supprimer Pret" tab
pret_id_label = tk.Label(supprimer_pret_tab, text="ID du Prêt:")
pret_id_label.pack()

pret_id_entry = tk.Entry(supprimer_pret_tab)
pret_id_entry.pack()

supprimer_pret_button = tk.Button(supprimer_pret_tab, text="Supprimer Prêt", command=supprimer_pret)
supprimer_pret_button.pack()

# Add the "Supprimer Pret" tab to the Tabbed Pane
tabbed_pane.add(supprimer_pret_tab, text="Supprimer Pret")

# Pack the Tabbed Pane widget
tabbed_pane.pack(expand=1, fill="both")

# Start the Tkinter event loop
window.mainloop()
