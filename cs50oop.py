class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Eagle","Impala","Zebra","CHeetah","Flamingo"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
         
            

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name.capitalize(), house.capitalize())
    
if __name__ == "__main__":
    main()

# [1:24:00]
