# Python uses * and ** as visual indicator when a function might take variable number of arguments
# *args → variable number of positional arguments
# **kwargs → variable number of keyword arguments (named parameters) that can be called by their name


# Prints positional arguments
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)


# Prints named arguments
def g(*args, **kwargs):
    print("Named:", kwargs)

g(galleons=100, sickles=50, knuts=25)
