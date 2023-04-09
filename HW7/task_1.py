my_phone_book = {}

def stats():
    print("number of contacts: ", len(my_phone_book))

def add():
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    if name in my_phone_book:
        print("This contact is already registered!")
    else:
        my_phone_book[name] = number
        print("Contact added successfully")

def delete(name):
    if name in my_phone_book:
        del my_phone_book[name]
        print("Contact deleted successfully")
    else:
        print("Not found")

def list_contacts():
    for name in my_phone_book:
        print(name)

def show(name):
    if name in my_phone_book:
        print("Name: ", name)
        print("Phone number: ", my_phone_book[name])
    else:
        print("Contact not found")

while True:
    command = input("Enter the command (stats, add, delete, list, show): ")
    if command == "stats":
        stats()
    elif command == "add":
        add()
    elif "delete" in command:
        name = command.split()[1]
        delete(name)
    elif command == "list":
        list_contacts()
    elif "show" in command:
        name = command.split()[1]
        show(name)
    else:
        print("Oops... Something goes wrong! Try again")
