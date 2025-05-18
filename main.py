
from db import add_contact , list_contacts , delete_contact , edit_contact

def main():
    while True:
        print("\nSimple Contact Book")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Delete contact")
        print("4. Edit contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            name_to_delete = input("Enter the name of the contact to delete: ")
            delete_contact(name_to_delete)
        elif choice == "4":
            name_to_edit = input("Enter the name of the contact to edit: ")
            edit_contact(name_to_edit)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
