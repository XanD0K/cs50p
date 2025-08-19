import csv

students = []

with open("students1.csv") as file:
    # reader() function reads a .csv file, and deals with commas and any corner cases that might appear
    reader = csv.reader(file) 
    for name, home in reader: # Instead of that unpackle, you can use 'row', and access those values with row[0] and row[1]
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

