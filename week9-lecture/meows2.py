# Demonstrates TypeError


def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)

# Python is a dynamically typed language
# You don't have to specify the variable type before declaring/using it
# You can run the program and see the error it will prompt
# Alternatively, you can add "type hints" to the code and run a program to check those hints (e.g. mypy)
# ': int' is a type hint. It's just a hint, an annotation, that the variable on the left should be an int
# It doesn't change the variable neither prompts any error. It just a hint to the programmer
# Programs like 'mypy' can access those hints to check for errors
# It's a tool that the programmer would run before releasing the code
# In terminal:
## 'pip install mypy'
## mypy meows.py 