# There's a newer and improved version on 'pset5' directory

def main():
    numer, denom = get_fraction()
    fuel = round((numer / denom) * 100)        

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

    
def get_fraction():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))                     
            if x > y:
                print("Denominator must be higher than numerator")
                continue
            elif x < 0 or y < 0:
                print("Enter positive numbers!")
                continue   
            elif y == 0:
                print("Denominator can't be '0'! Choose another number!")            
            return x, y
        except ValueError:
            print("Enter a valid input!")        

if __name__ == "__main__":
    main()