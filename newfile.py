import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Retrieve form data
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    # Validate form data
    if not (name and email and password and confirm_password):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    
    # Process the form data (in this case, just printing)
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)
    print("Confirm Password:", confirm_password)
    
    # Optionally, you can save the data to a file or database here
    
    # Show success message
    messagebox.showinfo("Success", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place form elements
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Password:").grid(row=2, column=0, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)

tk.Label(root, text="Confirm Password:").grid(row=3, column=0, sticky="e")
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=2)

# Start the GUI event loop
root.mainloop()
