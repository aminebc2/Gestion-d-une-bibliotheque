import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Function to handle user login
def user_login(user_type):
    def perform_user_login():
        username = username_entry.get()
        password = password_entry.get()

        # Connect to the database and perform user login checks
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Execute the query to check user credentials based on user type
        if(user_type=="admin") : cursor.execute("SELECT * FROM admins WHERE login=? AND password=? ", (username, password))
        else: cursor.execute("SELECT * FROM users WHERE nom=? AND prenom=? ", (username, password))
        user_data = cursor.fetchone()

        if user_data:
            messagebox.showinfo("User Login", f"{user_type.capitalize()} login successful!")
            user_window(user_type)
        else:
            messagebox.showerror("User Login", "Invalid credentials!")

        conn.close()

    # Create the user login window
    user_login_window = tk.Tk()
    user_login_window.title(f"{user_type.capitalize()} Login")
    user_login_window.geometry("300x200")

    # Add labels and entry fields for username and password
    username_label = ttk.Label(user_login_window, text=f"{user_type.capitalize()} Username:")
    username_label.pack()
    username_entry = ttk.Entry(user_login_window)
    username_entry.pack()

    password_label = ttk.Label(user_login_window, text=f"{user_type.capitalize()} Password:")
    password_label.pack()
    password_entry = ttk.Entry(user_login_window, show="*")
    password_entry.pack()

    # Add a login button
    login_button = ttk.Button(user_login_window, text="Login", command=perform_user_login)
    login_button.pack()

    # Start the user login window event loop
    user_login_window.mainloop()

# Function to handle user window
def user_window(user_type):
   
   if(user_type=="adherent") :import library_management_adh
   if(user_type=="admin") :import library_management_admin
   if(user_type=="bibliothecaire") :import library_management_biblio

# Create the database and tables


# Start the program by displaying the user type choice window
choice_window = tk.Tk()
choice_window.title("User Type")
choice_window.geometry("300x200")

# Add labels and buttons for admin, adherent, and bibliothecaire login options
admin_label = tk.Label(choice_window, text="Admin Login")
admin_label.pack()

admin_button = tk.Button(choice_window, text="Admin", command=lambda: user_login("admin"))
admin_button.pack()

adherent_label = tk.Label(choice_window, text="Adherent Login")
adherent_label.pack()

adherent_button = tk.Button(choice_window, text="Adherent", command=lambda: user_login("adherent"))
adherent_button.pack()

bibliothecaire_label = tk.Label(choice_window, text="Bibliothecaire Login")
bibliothecaire_label.pack()

bibliothecaire_button = tk.Button(choice_window, text="Bibliothecaire", command=lambda: user_login("bibliothecaire"))
bibliothecaire_button.pack()

# Start the choice window event loop
choice_window.mainloop()