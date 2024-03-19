students = []

with open("students.csv") as f:
    for line in f:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
