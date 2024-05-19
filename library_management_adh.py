import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

def reserve_book(book_id):
    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check the availability of the book
    cursor.execute("SELECT status FROM livres WHERE id=?", (book_id,))
    book_status = cursor.fetchone()

    if book_status and book_status[0] == "dispo":
        # Update the book status to "reserved"
        cursor.execute("UPDATE livres SET status='reserved' WHERE id=?", (book_id,))
        # inserer dans la table reservation la nouvelle reservation   cursor.execute("INSERT IN reservations status='reserved' WHERE id=?", (book_id,))
        conn.commit()

         # Insert a new reservation user_id=1
        cursor.execute("INSERT INTO reservations (id_livre, id_user) VALUES (?, ?)", (book_id, 1))
        conn.commit()

        messagebox.showinfo("Book Reservation", "Book reserved successfully!")
    else:
        messagebox.showerror("Book Reservation", "Book is not available for reservation.")

    # Close the database connection
    conn.close()

def display_books():
    # Connect to the database
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Fetch all books from the livres table
    cursor.execute("SELECT id, titre, status FROM livres")
    books = cursor.fetchall()

    # Remove existing treeview if it exists
    for child in treeview_frame.winfo_children():
        child.destroy()

    # Create a treeview widget
    treeview = ttk.Treeview(treeview_frame, columns=("BookID", "Title", "Status"), show="headings")
    treeview.pack(side="left", fill="both", expand=True)

    # Configure the columns
    treeview.column("BookID", width=50)
    treeview.column("Title", width=200)
    treeview.column("Status", width=100)

    # Define the headings
    treeview.heading("BookID", text="ID")
    treeview.heading("Title", text="Title")
    treeview.heading("Status", text="Status")

    # Insert the book data into the treeview
    for book in books:
        treeview.insert("", "end", values=book)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")
    treeview.configure(yscrollcommand=scrollbar.set)

    # Add a Reserve button
    reserve_button = ttk.Button(button_frame, text="Reserve", command=lambda: reserve_book(treeview.item(treeview.selection())["values"][0]))
    reserve_button.pack(side="left")

    # Close the database connection
    conn.close()

# Create the main application window
window = tk.Tk()
window.title("Library Management System - Adherent")

# Create a frame for the treeview and scrollbar
treeview_frame = ttk.Frame(window)
treeview_frame.pack(fill="both", expand=True)

# Create a frame for the Reserve button
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

# Display the books
display_books()

# Start the application event loop
window.mainloop()