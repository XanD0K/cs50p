from datetime import date, datetime

import inflect
import sys


def main():
    p = inflect.engine()

    birth_date = input("Date of Birth: ").strip()
    if not validate_date(birth_date):
        sys.exit("Invalid date! Format: YYYY-MM-DD")

    minutes = minutes_since_birth(birth_date)
    if not minutes:
        sys.exit("Invalid date!")

    print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")


def validate_date(d):
    try:
        birth = datetime.strptime(d, "%Y-%m-%d")
        if birth.date() > date.today():
            return False
        return True
    except ValueError:
        return False


def minutes_since_birth(birth):
    try:
        birth_date = date.fromisoformat(birth)
        today = date.today()
        return (abs(today - birth_date).days * 24 * 60)
    except ValueError:
        return None


if __name__ == "__main__":
    main()


# TODO: accept more date formats
# TODO: accept time → use total_seconds()