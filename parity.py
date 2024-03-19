#this programs checks whether a number is an even number or an odd number

a = int(input("Please enter a number:"))
if a % 2 == 1:
    print(a, "is an odd number")
else:
    print(a, "is an even number")