class Student:
    def __init__(self, name, house):  
        self.name = name
        self.house = house

    def __str__(self):
         return f"{self.name} from {self.house}"   

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter (function that gets some attribute)
    @property
    def house(self):
        return self._house
    
    # Setter (function that sets some value)
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
  

def main():
    student = get_student()    
    # Python focuses on conventions, not hard constraints
    # You can decide if an instance variables will be public, accessible in code, protected, or private
    # The convention is: if an instance variable starts with an underscore, don't touch it
    # But nothing prevents to change that value:
    student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house, ) 


if __name__ == "__main__":
    main()