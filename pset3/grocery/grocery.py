def main():
    groceries = get_grocery()
    # .items() return a tuple for every item. Using tuple unpackle to access its values
    for item, count in sorted(groceries.items()):
        print(f"{count} {item}")

def get_grocery():
    print("Enter your grocery list:")
    groceries = {}
    while True:
        try:
            grocery = input().upper()
            # No input was made
            if not grocery:
                print("Enter an item first!")
                continue
            # Allow spaces, but prevent numbers and symbols
            if not grocery.replace(" ", "").isalpha():
                print("Enter a valid word!")
                continue
            # Get user's input to set as a key in the dict. If exists, use its value, otherwise, use '0' as default
            groceries[grocery] = groceries.get(grocery, 0) + 1

        except (EOFError, KeyboardInterrupt):
            print()
            return groceries

if __name__ == "__main__":
    main()
