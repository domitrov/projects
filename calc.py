def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a, b):
    while True:
        try:
            result = a / b
        except ZeroDivisionError:
            print("Zero Division Error")
        else:
            break
    return result

def multiply(a,b):
    return a * b



def mian():

    operation = input("Select an opration\nmultiply\nadd\nsubtract\ndivide\n--> ")

    a = float(input("First number: "))
    b = float(input("Second number: "))


    if operation == "add":
        print(add(a,b))
    elif operation == "subtract":
        print(subtract(a,b))
    elif operation == "multiply":
        print(multiply(a,b))
    elif operation == "divide":
        print(divide(a,b))        


if __name__ == "__main__":
    mian()
