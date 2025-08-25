# Uses filter() function to filter students
# To sorte, uses key with lambda

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


# filter() takes at least 2 arguments: the name of a function to call (that returns True/False), and the sequence of elements
# It's similar to map(), but map applies the function to all elements
gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
