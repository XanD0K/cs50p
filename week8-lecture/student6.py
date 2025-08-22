class Student:
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
         return f"{self.name} from {self.house}"
    
    # We want to prevent programmers/users to circumventing those error checks above for 'name' and 'house'
    # We want to prevent changing a value that doesn't follows those checks (e.g. student.house = "Number Four, Privet Drive")
    # Let's require that, in order to set some attribute and to access an attribute, you go through some function (Getter and Setter functions)

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
    # Now, when user tries to access student.house, Python will automatically calls that Setter function
    # It does so if on the left side we have the name of the Getter/Setter, with and equal sign indicating assignment (e.g. student.house = "Number Four (...)")
    # To do that, we also need to use a decorator (@)
    
    # Property is an attribute to give you more control over that class
    # It allows to decorate functions. In other words, it's a function that modifies the behavior of other functions

    # @property defines the getter, and you name the function exactly like you would like the property to be called
    # @<property_name>.setter defines the setter
    # Can't have variable 'house' and function 'house', so changed to _house
    # That way the instance variable is '_house' and the property is 'house'
    # '@property def house' lets access sudent.house, like an attribute
    # The actual data is stored in a separate attribute, in this case, self._house
    # Use double underscore instead to make it Private, by triggering Python's name mangling
    # Just like single underscore, double underscore doesn't prevent acessing from outside of the class. "Python trusts developers to follow conventions"

def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive" → with those decorators, that code won't work
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house, ) 


if __name__ == "__main__":
    main()