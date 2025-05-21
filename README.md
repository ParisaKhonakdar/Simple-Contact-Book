# 📒 Simple Contact Book

A beginner-friendly command-line contact manager written in Python. Easily add, view, edit, and delete your contacts — all stored locally in a lightweight JSON file.

##  Features

-  Add new contacts (name & phone number)
-  View all saved contacts
-  Edit existing contacts
-  Delete contacts you no longer need
-  Data saved in a local `contacts.json` file
-  Includes basic error handling

###  Requirements
- Python 3.x installed on your system

###  Run the app

Clone the repository and run the app using:

```bash
python main.py
```

##  Menu Options

Once you run the program, you'll see:

```
Simple Contact Book
1. Add contact
2. List contacts
3. Delete contact
4. Edit contact
5. Exit
```
Just type the number for the action you want and follow the prompts!

##  File Structure

```
Simple-Contact-Book/
│
├── main.py         # The main CLI interface
├── db.py           # Handles contact data (load/save/edit/delete)
├── contacts.json   # Stores your contact data
└── README.md       # This file
```

##  Why JSON?

We use a simple `contacts.json` file to store data. It's human-readable, easy to back up, and avoids needing a database — perfect for small CLI tools like this.

##  Contact

Created by [Parisa](https://github.com/ParisaKhonakdar)