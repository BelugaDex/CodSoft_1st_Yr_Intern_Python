import json
import os

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

def add_contact(contacts, name, phone_no, email, address):
    """Add a new contact."""
    contact_id = str(len(contacts) + 1)
    contacts[contact_id] = {
        "name": name,
        "phone_no": phone_no,
        "email": email,
        "address": address
    }
    print("Contact added with ID:", contact_id)

def update_contact(contacts, contact_id, name=None, phone_no=None, email=None, address=None):
    """Update an existing contact."""
    if contact_id in contacts:
        if name:
            contacts[contact_id]["name"] = name
        if phone_no:
            contacts[contact_id]["phone_no"] = phone_no
        if email:
            contacts[contact_id]["email"] = email
        if address:
            contacts[contact_id]["address"] = address
        print("Contact", contact_id, "updated.")
    else:
        print("Contact ID", contact_id, "not found.")

def delete_contact(contacts, contact_id):
    """Delete a contact."""
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact", contact_id, "deleted.")
    else:
        print("Contact ID", contact_id, "not found.")

def list_contacts(contacts):
    """List all contacts."""
    if contacts:
        for contact_id, details in contacts.items():
            print(f"ID: {contact_id}\nName: {details['name']}\nPhone Number: {details['phone_no']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
    else:
        print("No contacts found.")

def search_contacts(contacts, search_term):
    """Search contacts by name or phone number."""
    results = [details for details in contacts.values() if search_term in details['name'] or search_term in details['phone_no']]
    if results:
        for result in results:
            print(f"Name: {result['name']}\nPhone Number: {result['phone_no']}\nEmail: {result['email']}\nAddress: {result['address']}\n")
    else:
        print("No matching contacts found.")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Search Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_no = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_contact(contacts, name, phone_no, email, address)
            save_contacts(contacts)
        elif choice == '2':
            contact_id = input("Enter Contact ID to update: ")
            name = input("Enter New Name (leave blank to keep current): ")
            phone_no = input("Enter New Phone Number (leave blank to keep current): ")
            email = input("Enter New Email (leave blank to keep current): ")
            address = input("Enter New Address (leave blank to keep current): ")
            update_contact(contacts, contact_id, name if name else None, phone_no if phone_no else None, email if email else None, address if address else None)
            save_contacts(contacts)
        elif choice == '3':
            contact_id = input("Enter Contact ID to delete: ")
            delete_contact(contacts, contact_id)
            save_contacts(contacts)
        elif choice == '4':
            list_contacts(contacts)
        elif choice == '5':
            search_term = input("Enter name or phone number to search: ")
            search_contacts(contacts, search_term)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
