from datetime import date, datetime

import inflect
import sys


class MinutesBorn:
    def __init__(self, birth_date):
        self.p = inflect.engine()
        self.birth_date = birth_date
        if not self._validate_date():
            sys.exit("Date not valid! Format: YYYY-MM-DD")
    
    def _validate_date(self):
        try:
            datetime.strptime(self.birth_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def minutes_since_birth(self):
        try:
            _birth_date = date.fromisoformat(self.birth_date)
            minutes = (date.today() - _birth_date).days * 24 * 60
            return f"{self.p.number_to_words(minutes, andword='').capitalize()} minutes"
        except ValueError:
            sys.exit("Invalid date!")

        

def main():
    birth_date = input("Date of Birth: ").strip()
    print(MinutesBorn(birth_date).minutes_since_birth())


if __name__ == "__main__":
    main()