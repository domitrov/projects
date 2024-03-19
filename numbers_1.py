from num_id import nums

def main():
    try:
        n = int(input("Declare n: "))
        option = int(input("What would you like to do?\n1.List factors\n2.isPrime\n3.isOdd\n4.isTriangle\n5.isEven\n"))
    except ValueError:
        print("Invalid input. Please enter integers for option and n.")
        return

    if option == 1:
        print(nums.list_factors(n))
    elif option == 2:
        print(nums.isPrime(n))
    elif option == 3:
        print(nums.isOdd(n))
    elif option == 4:
        print(nums.isTriangle(n))
    elif option == 5:
        print(nums.isEven(n))
    else:
        print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
