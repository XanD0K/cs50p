import random

class Hat:
    # If not going to instanciate multiple Hat objects, don't need that '__init__' method
    # That's a class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Since it's only going to be one sorting hat, declare it as a class method
    # Instead of passing self, we pass 'cls', which is the reference to the class itself
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# With those changes, I don't need to instanciate any Hat object anymore
Hat.sort("Harry")

# That's the same logic of acessing a function (e.g. strip(), lower()) from the 'str' class