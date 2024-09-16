students = [
    {"name" : "Hermoine", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

students.sort()

for s in students:
    print(s["name"], s["house"], s["patronus"], sep=" | ")


