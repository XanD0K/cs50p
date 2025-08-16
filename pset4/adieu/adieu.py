import inflect

def main():
    p = inflect.engine()
    # Keep track of all names
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()
            if name:
                names.append(name)
        except (EOFError, KeyboardInterrupt):
            break

    # Using inflict's join method to format the output string
    if names:
        print("Adieu, adieu, to", p.join(names))
    else:
        print("Adieu, adieu, to nobody!")
        

if __name__ == "__main__":
    main()