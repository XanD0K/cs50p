# A class can inherit from another class, which means it can "borrow" attributes (methods/variables) from another

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

# That means that the Student class is a subclass of Wizard
# In other words, Wizard is the superclass of the Student class
class Student(Wizard): 
    def __init__(self, name, house):
        # super() is a way of acessing the superclass (parent class)
        # __init__ refers to that class's own initialization method
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

# That is applied to the ideia of "Exceptions" in Python
# All exceptions (e.g. ValueError, NameError, SyntaxError) are classes that inherits from the "Exception" superclass
# That 'Exception' class, meanwhile, also has a parent class called "BaseException"