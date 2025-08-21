import validators


def main():
    email = input("What's your email address? ").strip()
    print(validate(email))


def validate(email):
    return "Valid" if validators.email(email) else "Invalid"


if __name__ == "__main__":
    main()
