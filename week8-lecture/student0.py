def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")

    return name, house 
    # That returns a tupple.
    # Tupples are immutable, which means you can't change it's value!
    # If want to change, return it as a list (e.g. return [name, house])


if __name__ == "__main__":
    main()