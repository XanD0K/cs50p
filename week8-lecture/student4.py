class Student:
    # Method used to initialize the contens of an object from a class
    # The __init__ method is also called "constructor"
    def __init__(self, name, house):
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # That's a constructor call, which purpose is to construct (instantiate) a Student object
    student = Student(name, house) 
    return student


if __name__ == "__main__":
    main()