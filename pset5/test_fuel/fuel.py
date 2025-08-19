def main():
    try: 
        fraction = input("Fraction: ")
        if not fraction:
            print("Enter a fraction")
        converted_fraction = convert(fraction)
        print(gauge(converted_fraction))
    except (ValueError, ZeroDivisionError) as error:
        print(error)


# Conver fraction to a percentage value
def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:        
        raise ZeroDivisionError("Denominator can't be zero")
    elif x > y:
        raise ValueError("Numerator can't be higher than denominator")
    elif x < 0 or y < 0:
        raise ValueError("Provide positive integers")

    return round(x/y * 100)


# Receives a percentage value to decide what will appear in the fuel gauge
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()