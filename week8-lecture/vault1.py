# Operator Overloadin
# You can take commom symbols (e.g. plus, minus) and implement your own interpretation thereof
# '+' does not have to mean "addition". It can also mean concatenation

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
# To do this, we'll use the method 'object.__add__(self, other)'
# It takes, by convention, 'self' as a first argument, and another argument as a second argument, which by convention is called 'other'
# 'self' makes reference to the left operand, which is whatever object on the left of a '+' sign
# 'other' makes reference to the right operand, which is whatever object on the right of a '+' sign
print(total)
