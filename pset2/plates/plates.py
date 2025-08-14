def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Plate must have between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False
    # First 2 characters must be letters
    if not s[:2].isalpha():
        return False
    # Only letters and numbers (exclude ponctuations, periods, spaces)
    if not s.isalnum():
        return False
    # Check for numbers
    # Variable to keep track of the first number that appears in the plate
    decimal = False
    for char in s:
        if char.isdecimal():
            # Firs number is 0
            if char == "0" and not decimal:
                return False
            # If first number is not a 0, set 'decimal' to True
            # It will allow zero to appear later
            decimal = True
        # There was numbers ('decimal' set to True), and then a letter appears after that number
        elif decimal:
            return False
    # Either no numbers appeared OR passed all previous number checks
    return True     
    
if __name__ == "__main__":
    main()