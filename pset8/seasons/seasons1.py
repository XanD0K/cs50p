from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

def main():
    birth_input = input("Date of Birth: ").strip()
    birth = parse_birth_date(birth_input)
    if birth is None:
        sys.exit("Invalid date! Format: YYYY-MM-DD")

    minutes = minutes_between(birth, date.today())
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


# Parse a date string YYYY-MM-DD into a date, or return None on error or future date
def parse_birth_date(d: str):
    try:
        birth = datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        return None
    return birth if birth <= date.today() else None


# Return number of minutes between two dates (assumed at midnight)
def minutes_between(start_date, end_date):
    start_dt = datetime.combine(start_date, datetime.min.time())
    end_dt = datetime.combine(end_date, datetime.min.time())
    return int((end_dt - start_dt).total_seconds() / 60)


if __name__ == "__main__":
    main()