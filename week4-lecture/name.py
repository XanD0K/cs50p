import sys

# Check for errors (I could also try-except to execute the file)
if len(sys.argv) < 2:
    # sys.exit exits the program
    sys.exit("Too few arguments. Usage: python name.py <your_name>")


# Print name tags
print("hello, my name is", sys.argv[1])
# argv[0] is the program's name itself 

print()

for arg in sys.argv:
    print(arg)

print()

for arg in sys.argv[1:]:
    print(arg)