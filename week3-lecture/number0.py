try: 
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
# Only executed if 'try' succeeds
# Prevents NameError if user assigns an invalid value to 'x'
else:
    print(f"x is {x}")