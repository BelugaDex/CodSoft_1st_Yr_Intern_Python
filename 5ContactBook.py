import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to save contacts
CONTACT_FILE = "contacts.json"


def load_contacts():
    """Load contacts from a file."""
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    """Add a new contact."""
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone_no = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    if name and phone_no and email and address:
        contact_id = str(len(contacts) + 1)
        contacts[contact_id] = {
            "name": name,
            "phone_no": phone_no,
            "email": email,
            "address": address
        }
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact added with ID: {contact_id}")
        list_contacts()
    else:
        messagebox.showerror("Error", "All fields are required!")


def update_contact():
    """Update an existing contact."""
    contact_id = simpledialog.askstring("Update Contact", "Enter Contact ID to update:")

    if contact_id in contacts:
        name = simpledialog.askstring("Update Contact", "Enter New Name (leave blank to keep current):")
        phone_no = simpledialog.askstring("Update Contact", "Enter New Phone Number (leave blank to keep current):")
        email = simpledialog.askstring("Update Contact", "Enter New Email (leave blank to keep current):")
        address = simpledialog.askstring("Update Contact", "Enter New Address (leave blank to keep current):")

        if name:
            contacts[contact_id]["name"] = name
        if phone_no:
            contacts[contact_id]["phone_no"] = phone_no
        if email:
            contacts[contact_id]["email"] = email
        if address:
            contacts[contact_id]["address"] = address

        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {contact_id} updated.")
        list_contacts()
    else:
        messagebox.showerror("Error", f"Contact ID {contact_id} not found.")


def delete_contact():
    """Delete a contact."""
    contact_id = simpledialog.askstring("Delete Contact", "Enter Contact ID to delete:")

    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {contact_id} deleted.")
        list_contacts()
    else:
        messagebox.showerror("Error", f"Contact ID {contact_id} not found.")


def list_contacts():
    """List all contacts."""
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    if contacts:
        for contact_id, details in contacts.items():
            text_area.insert(tk.END,
                             f"ID: {contact_id}\nName: {details['name']}\nPhone Number: {details['phone_no']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n")
    else:
        text_area.insert(tk.END, "No contacts found.")
    text_area.config(state=tk.DISABLED)


def search_contacts():
    """Search contacts by name or phone number."""
    search_term = simpledialog.askstring("Search Contacts", "Enter name or phone number to search:")

    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    results = [details for details in contacts.values() if
               search_term in details['name'] or search_term in details['phone_no']]
    if results:
        for result in results:
            text_area.insert(tk.END,
                             f"Name: {result['name']}\nPhone Number: {result['phone_no']}\nEmail: {result['email']}\nAddress: {result['address']}\n\n")
    else:
        text_area.insert(tk.END, "No matching contacts found.")
    text_area.config(state=tk.DISABLED)


# Load contacts
contacts = load_contacts()

# Create the main window
root = tk.Tk()
root.title("Contact Book Application")
root.configure(bg='#282828')  # Background color

# Create a text area for displaying contacts
text_area = tk.Text(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED, bg='#1e1e1e', fg='#ffffff')
text_area.pack(pady=10)

# Create buttons for actions
button_frame = tk.Frame(root, bg='#282828')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, bg='#007acc', fg='#ffffff',
                       activebackground='#005f99', activeforeground='#ffffff')
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact, bg='#007acc', fg='#ffffff',
                          activebackground='#005f99', activeforeground='#ffffff')
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, bg='#007acc', fg='#ffffff',
                          activebackground='#005f99', activeforeground='#ffffff')
delete_button.grid(row=0, column=2, padx=5, pady=5)

list_button = tk.Button(button_frame, text="List Contacts", command=list_contacts, bg='#007acc', fg='#ffffff',
                        activebackground='#005f99', activeforeground='#ffffff')
list_button.grid(row=1, column=0, padx=5, pady=5)

search_button = tk.Button(button_frame, text="Search Contacts", command=search_contacts, bg='#007acc', fg='#ffffff',
                          activebackground='#005f99', activeforeground='#ffffff')
search_button.grid(row=1, column=1, padx=5, pady=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.quit, bg='#007acc', fg='#ffffff',
                        activebackground='#005f99', activeforeground='#ffffff')
exit_button.grid(row=1, column=2, padx=5, pady=5)

# Start the Tkinter event loop
list_contacts()
root.mainloop()
