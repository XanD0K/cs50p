# Uses global

balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()


# You can read global variables
# But to change them, you need to use the keyword 'global' in the specific function
# Withtout it, it will raise an 'UnboundLocalError'
