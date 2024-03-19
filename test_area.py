from time import sleep

# Password Verification
for attempt in range(5):
    entry = input("Password: ")
    if entry == "her":
        print("Password correct, please wait.")
        for _ in range(3):
            print(".", end="\n")
            sleep(0.9)
        break
    print(f"Attempt {attempt}/4")
    if attempt == 4:
        exit("Too many attempts\nExiting program....")

print("Welcome Justin")

# Entry Management
entry_list = []

def add_entry():
    
    inp = input("Enter data:\n")
    
    entry_list.append(inp)

def display_entries():
    for index, item in enumerate(entry_list):
        print(f"{index + 1}. {item}")

def edit_entries():
    display_entries()
    while True:    
        try:
            entry_index = int(input("Select entry to edit: "))
        except:
            print("Enter one integer")
        else:
            break    
    print(entry_list[entry_index - 1])
    new_entry = input("Enter a new entry below:\n")
    entry_list[entry_index - 1] = new_entry
    display_entries()

def erase_entry():
    display_entries()
    while True:
        try:
            entry_to_erase = int(input("Which entry would you like to erase? "))
        except ValueError:
            print("Enter only one integer")
        else:
            break  
    if 1 <= entry_to_erase <= len(entry_list):
        entry_list.pop(entry_to_erase - 1)
        print(f"Entry {entry_to_erase} has been erased.")
    else:
        print("Invalid entry index.")

while True:
    print("1. Add entry\n2. Erase entry\n3. Edit entries\n4. Display entries\n5. Exit")
    while True:    
        try:
            selection = int(input("Select an option to begin: "))
        except ValueError:
            print("Enter only one integer")
        else:
            break


    if selection == 1:
        add_entry()
    elif selection == 2:
        erase_entry()
    elif selection == 3:
        edit_entries()
    elif selection == 4:
        display_entries()
    elif selection == 5:
        break
    else:
        print("Invalid selection. Please choose a valid option.")

print("Please wait, program is exiting")
for i in range(5):
    sleep(0.9)
    print(i + 1 , end="...")

exit()