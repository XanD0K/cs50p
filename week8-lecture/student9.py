# Moves get_student into Student class


# All things related to the student comes in here
# That's the reason to move get_student() funciton into this class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # That  decorators allows to call this method without instantiating a Student object first
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()


# There are other types of methods in Python's classes
# They tend to be called "statis methods", and they have the @staticmethod decorator
# Use @staticmethod for methods that don’t need access to self or cls
# A @staticmethod is a method that belongs to a class but doesn’t receive self or cls as an argument
# It’s a regular function scoped to the class’s namespace, used for utility functions related to the class
""" e.g.
class Student:
    @staticmethod
    def is_valid_house(house):
        return house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

class Student:
    @staticmethod
    def format_name(name):
        return name.title()  # Capitalizes name      
"""

