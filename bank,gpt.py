import sys
from datetime import datetime
import getpass
from time import sleep
balance_file = "balance.txt"
log_file = "transaction_log.txt"
correct_password = "justin2007"

def deposit():
    global balance
    try:
        dep_amnt = float(input("How much would you like to deposit?\nAmount: "))
    except ValueError:
        print("Invalid input. Enter a valid amount.")
        return 
    balance += dep_amnt
    with open(balance_file, "w") as f:
        f.write(str(balance))
    
    log_transactions("Deposit", dep_amnt)

    return round(balance, 2)

def withdraw():
    global balance
    try:
        wit_amnt = float(input("How much would you like to withdraw?\nAmount: "))
    except ValueError:
        print("Invalid input. Enter a valid amount.")
        return

    if wit_amnt > balance:
        print("Insufficient funds.")
        return

    balance -= wit_amnt
    with open(balance_file, "w") as f:
        f.write(str(balance))
    
    log_transactions("Withdrawal", wit_amnt)

    return round(balance, 2)

def display_balance():
    try:
        with open(balance_file) as f:
            for line in f:
                balance = float(line)
        print(f"Your balance is ${balance:.2f}")
    except FileNotFoundError:
        print("Balance file not found.")

def log_transactions(transaction_type, amount):
    try:
        with open(log_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {transaction_type}: ${amount:.2f}\n")
    except Exception as e:
        print(f"Error logging transaction: {e}")

def view_transaction_log():
    try:
        with open(log_file) as f:
            print("Transaction Log:")
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print("Transaction log not found.")

def main():
    for _ in range(1, 6):
        password = getpass.getpass("Password: ")
        if password == correct_password:
            break
        elif _ == 5:
            sys.exit("Too many attempts.")
    
    print(datetime.now())
    
    while True:
        try:
            option = int(input("What would you like to do?\n1. Deposit\n2. Withdraw\n3. View Balance\n4. View Transaction Log\n5. Exit\n\n[Please enter the option index number]\n"))
        except ValueError:
            print("Enter a valid option number.")

        if option == 1:
            deposit()
        elif option == 2:
            withdraw()
        elif option == 3:
            display_balance()
        elif option == 4:
            view_transaction_log()
        elif option == 5:
            for i in range(1,4):
                print(i, end="\r")
                sleep(1.0)
            sys.exit("Program terminated")

if __name__ == "__main__":
    balance = 0
    main()
