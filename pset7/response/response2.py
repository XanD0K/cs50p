from email_validator import validate_email, EmailNotValidError


def main():
    email = input("What's your email address? ").strip()
    print(validate(email))


def validate(email):
    try:
        validate_email(email, check_deliverability=False)
        return "Valid"
    except EmailNotValidError:
        return "Invalid"


if __name__ == "__main__":
    main()
