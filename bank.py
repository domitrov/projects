import sys
from datetime import datetime, date, time, timedelta, timezone
import getpass as gt
balance = 0

def deposit():
    global balance
    dep_amnt = float(input("How much would you like to deposit?\nAmount: "))
    balance += dep_amnt
    with open("balance.txt", "w") as f:
        f.write(str(balance))  # Convert balance to string before writing to the file
    return round(balance, 2)

def withdraw():
    #add functionality of withdrawing all or own amount
    global balance
    _ = int(input("1.Withdraw all\n2.Withdraw own amount\n:"))
    if _ == 1:
        with open("balance.txt") as f:
           line = f.readline()
             

def display_balance():
    with open("balance.txt") as f:
        for line in f:
            balance = float(line)  # Convert the string back to float
    print("Your balance is", round(balance, 2))


def log_transcations():
    pass

def view_transaction_log():
    pass
# Password check

correct_password = "justin2007"


def main():
    for _ in range(1, 6):
        password = gt.getpass("Password: ")
        if password == correct_password:
            break
        elif _ == 5:
            sys.exit("Too many attempts.")
    current_date = datetime.now()
    print(current_date)
    while True:
        try:

            option = int(input("What would you like to do?\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Exit\n\n[Please enter the option index number]\n"))
        except ValueError:
            print("Enter a valid option number.")

        if option == 1:
            deposit()
        elif option == 2:
            withdraw()
        elif option == 3:
            display_balance()
        elif option == 4:
            sys.exit("Program terminated")




if __name__ == "__main__":
    main()