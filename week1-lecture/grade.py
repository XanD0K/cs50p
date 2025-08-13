score = int(input("Score: "))

# Demonstrates fewer comparisons
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# More 2 ways to do those checks:
# if score >= 90 and score <= 100:
# if 90 <= score <= 100:
