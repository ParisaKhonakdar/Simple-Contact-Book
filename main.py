from db import add_contact, list_contacts

def main():
    while True:
        print("\nSimple Contact Book")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
