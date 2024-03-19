#password = input("Password: ")
#while password != "1234":
#    print("Incorrect, please try again!")
#    password = input("Password: ")
#print("Password is correct")



def main():
    while True:
        n = int(input("What is n? "))
        if n < 0:
            continue
        else:
            break
    print("meow\n" * n, end="")  


    