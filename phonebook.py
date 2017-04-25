#!/usr/bin/env python3

import pickle

# creates the menu
def print_menu():
    print("="*29)
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Save entries")
    print("6. Restore saved entries")
    print("7. Quit")

# list all entries if dictionary is not empty
def list_entries(data):
    if data == {}:
        print("No entries found.")
    else:
        for key, value in data.items(): #get the key and value from all the dictionary items
            print("Found entry for {name}: {number}.".format(name=key, number=value))

# deletes an item, if existent, according to the user input
def del_entry(data):
    name = name_input()
    try:
        data.pop(name)
        print("Deleted entry for {}.".format(name))
    except KeyError:
        print("Please enter a valid entry.")

# creates an entry with the user input for name and phone number
def set_entry(data):
    name = name_input()
    number = phone_input()
    data[name] = number
    print("Entry stored for {}.".format(name))

# gets name from user input
def name_input():
    return input("Name: ")

# gets phone number from user input
def phone_input():
    return input("Phone Number: ")

# looks up for the phone number according to the name input
def look_up(data):
    name = name_input()
    try:
        print("Found entry for {name}: {number}.".format(name=name, number=data[name]))
    except KeyError:
        print("Name not in the list.")


# reads from a pickle file and returns the data
def read_from_pickle_file(FILENAME):
    with open(FILENAME, "rb") as fh:
        data = pickle.load(fh)
    return data

# writes data assigned to a pickle file
def write_to_pickle_file(FILENAME, data):
    with open(FILENAME, "wb") as fh:
        pickle.dump(data, fh)

def main():
    FILENAME = "phonebook.pickle" # file name and address
    try: # tries to get the data from the pickle file
        data = read_from_pickle_file(FILENAME)
    # if the file doesn't exit, creates it and appends an empty dictionary
    except EOFError:
        data = {}
        write_to_pickle_file(FILENAME, data)
    print(data) #debug
    quit = False
    while quit == False:
        print_menu()
        check = False
        while True: # receives the user input and checks if it is an integer betwenn 1 and 7
            user_input = input("What do you want to do (1-7)? ")
            try:
                if int(user_input) < 1 or int(user_input) > 7:
                    print("Enter a valid number.")
                else:
                    break
            except ValueError:
                print("Enter a valid number.")
        # select the choice of action according to the user's input
        if user_input == "1":
            data = look_up(data)
        elif user_input == "2":
            set_entry(data)
        elif user_input == "3":
            del_entry(data)
        elif user_input == "4":
            list_entries(data)
        elif user_input == "5":
            write_to_pickle_file(FILENAME, data)
            print("Entries saved to {}.".format(FILENAME))
        elif user_input == "6":
            data = read_from_pickle_file(FILENAME)
            print("Restored saved entries")
        elif user_input == "7":
            quit = True
        print()



if __name__ == "__main__":
    main()
