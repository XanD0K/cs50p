x = float(input("What's x? "))
y = float(input("What's y? "))

print(f"{round(x + y):,}")
# .round() → takes a number as input and round it to the closest integer
# :, → automatically adds a comma (,) after every group of 3 digits

print(f"{round((x / y), 2):,}")
# '2' inside of the round() function specifies the number of decimals

print(f"{(x / y):.2f}")
# :.2f → also specifies the number of decimals to be shown