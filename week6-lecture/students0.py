with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


print()

# Just like we did in 'names2_read.py', let's sort those names
students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# That 'lambda' function doesn't need 'def', neither a name
# It takes a parameter, which in this called was called 'student'
# And it returns the key "name"  for every dictionary