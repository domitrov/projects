import sys

if len(sys.argv[1])  < 2:
    print("too few arguments")
elif len(sys.argv[1]) > 2:
    print("too many arguments")
else:
    print(f"hello my name is {sys.argv[1]}")