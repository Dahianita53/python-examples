# 1
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# 2 
students = ["Hermione", "Harry", "Ron"]

for students in students:
    print(students)

# 3
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])

# 4
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i,students[i])

# 5 
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1,students[i])

# 6
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

# 7
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student)

# 8
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student,students[student])
    
# 9 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

# 10
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco","house": "Slytherin", "patronus": "None"}

]

for student in students:
    print(student["name"])

# 11 
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco","house": "Slytherin", "patronus": "None"}

]

for student in students:
    print(student["name"], student["house"])

# 12
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco","house": "Slytherin", "patronus": "None"}

]

for student in students:
    print(student["name"], student["house"], sep=", ")

# 13
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco","house": "Slytherin", "patronus": "None"}

]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
            
