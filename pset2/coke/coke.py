ALL_COINS = [25, 10, 5]

def main():
    coke_price = 50
    while coke_price > 0:
        print(f"Amount Due: {coke_price}")
        coin = insert_coin()
        if not (coke_price - coin <= 0):
            coke_price -= coin
            continue
        print(f"Change Owed: {abs(coke_price - coin)}")
        break


def insert_coin():
    while True:
        try:
            user_coin = int(input("Insert coin: "))
            if user_coin <= 0 or user_coin not in ALL_COINS:
                print("Insert a valid coin! Only allowed: 25, 10 and 5 coins!")
                user_coin = 0
            break
        except ValueError:
            print("That's not a valid number! Try again!")

    return user_coin


if __name__ == "__main__":
    main()


# TODO: keep track of amount_paid to simplify the code