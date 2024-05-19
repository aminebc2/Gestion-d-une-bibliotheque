import tkinter as tk
from tkinter import ttk
import sqlite3

def add_user():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    tel = tel_entry.get()
    adresse = adresse_entry.get()
    role = role_var.get()

    # Connect to SQLite database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Insert user data into the table
    cursor.execute("INSERT INTO users (nom, prenom, tel, adresse, role) VALUES (?, ?, ?, ?, ?)",
                   (nom, prenom, tel, adresse, role))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Clear the entry fields
    nom_entry.delete(0, tk.END)
    prenom_entry.delete(0, tk.END)
    tel_entry.delete(0, tk.END)
    adresse_entry.delete(0, tk.END)

    # Perform any other actions after adding the user
    print("User added successfully.")

def remove_user():
    user_id = id_entry.get()

    # Connect to SQLite database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Remove user from the table based on ID
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Clear the entry field
    id_entry.delete(0, tk.END)

    # Perform any other actions after removing the user
    print("User removed successfully.")

def search_users():
    # Connect to SQLite database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Fetch all users from the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Remove existing table if it exists
    for child in display_tab.winfo_children():
        child.destroy()

    # Create a treeview widget
    tree = ttk.Treeview(display_tab)

    # Define the table columns
    tree["columns"] = ("id", "nom", "prenom", "tel", "adresse", "role")

    # Format the table columns
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("id", anchor=tk.CENTER, width=50)
    tree.column("nom", anchor=tk.W, width=100)
    tree.column("prenom", anchor=tk.W, width=100)
    tree.column("tel", anchor=tk.W, width=100)
    tree.column("adresse", anchor=tk.W, width=150)
    tree.column("role", anchor=tk.W, width=100)

    # Create the table headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("id", text="ID", anchor=tk.CENTER)
    tree.heading("nom", text="Nom", anchor=tk.CENTER)
    tree.heading("prenom", text="Prenom", anchor=tk.CENTER)
    tree.heading("tel", text="Tel", anchor=tk.CENTER)
    tree.heading("adresse", text="Adresse", anchor=tk.CENTER)
    tree.heading("role", text="Role", anchor=tk.CENTER)

    # Insert the user data into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Pack the treeview widget
    tree.pack(fill="both", expand=True)

    # Create a Refresh button
    refresh_button = ttk.Button(display_tab, text="Refresh", command=search_users)
    refresh_button.pack()

    # Close the connection
    conn.close()




# Create the main application window
window = tk.Tk()
window.title("Library Management System")

# Create a tabbed pane
tab_pane = ttk.Notebook(window)

# Create individual tab windows
add_tab = ttk.Frame(tab_pane)
remove_tab = ttk.Frame(tab_pane)
display_tab = ttk.Frame(tab_pane)

# Add the tab frames to the tabbed pane
tab_pane.add(add_tab, text="Add")
tab_pane.add(remove_tab, text="Remove")
tab_pane.add(display_tab, text="Display")

# Add content to the "Add" tab
nom_label = ttk.Label(add_tab, text="Nom:")
nom_label.pack()
nom_entry = ttk.Entry(add_tab)
nom_entry.pack()

prenom_label = ttk.Label(add_tab, text="Prenom:")
prenom_label.pack()
prenom_entry = ttk.Entry(add_tab)
prenom_entry.pack()

tel_label = ttk.Label(add_tab, text="Tel:")
tel_label.pack()
tel_entry = ttk.Entry(add_tab)
tel_entry.pack()

adresse_label = ttk.Label(add_tab, text="Adresse:")
adresse_label.pack()
adresse_entry = ttk.Entry(add_tab)
adresse_entry.pack()

role_label = ttk.Label(add_tab, text="Role:")
role_label.pack()
role_var = tk.StringVar()
role_combobox = ttk.Combobox(add_tab, textvariable=role_var, values=["Adherent", "Bibliothecaire"])
role_combobox.pack()

add_button = ttk.Button(add_tab, text="Add User", command=add_user)
add_button.pack()

# Add content to the "Remove" tab
id_label = ttk.Label(remove_tab, text="Enter User ID:")
id_label.pack()
id_entry = ttk.Entry(remove_tab)
id_entry.pack()

remove_button = ttk.Button(remove_tab, text="Remove User", command=remove_user)
remove_button.pack()

# Add content to the "Display" tab
display_button = ttk.Button(display_tab, text="Search Users", command=search_users)
display_button.pack()

# Pack the tabbed pane
tab_pane.pack(expand=True, fill="both")

# Run the application
window.mainloop()
