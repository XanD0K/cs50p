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