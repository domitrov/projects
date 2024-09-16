def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("what is x? "))
        except ValueError:
            print("x is not an integer")
            
        # only breaks the loop if the user input is valid    
        else:
            break

main()