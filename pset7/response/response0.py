from validator_collection import validators, errors


def main():
    email = input("What's your email address? ").strip()
    print(validate(email))


def validate(email):
    try:
        email = validators.email(email)
        return "Valid"
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return "Invalid"


if __name__ == "__main__":
    main()
