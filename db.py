
import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Contact added: {name} - {phone}")

def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def delete_contact(name_to_delete):
    contacts = load_contacts()
    # Filter out contacts that match the name (case-insensitive)
    filtered_contacts = [c for c in contacts if c["name"].lower() != name_to_delete.lower()]

    if len(contacts) == len(filtered_contacts):
        print(f"No contact found with the name: {name_to_delete}")
    else:
        save_contacts(filtered_contacts)
        print(f"Contact '{name_to_delete}' deleted successfully.")
