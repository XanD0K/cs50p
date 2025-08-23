from datetime import date, datetime
import inflect
import sys
from typing import Optional, Literal


class DateConverter:
    def __init__(self, birth_date: str):
        self.p = inflect.engine()
        self.birth_date: str = birth_date.strip()
        if not self._validate_date():
            raise ValueError("Date not valid! Format: YYYY-MM-DD")

    def _validate_date(self) -> bool:
        try:
            datetime.strptime(self.birth_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def _get_date_difference(self, unit: Literal["days", "hours", "minutes"]) -> Optional[int]:
        try:
            birth_date = date.fromisoformat(self.birth_date)
            today = date.today()
            delta = today - birth_date
            if delta.days < 0:
                raise ValueError("Birth date cannot be in the future!")
            if unit == "days":
                return delta.days
            elif unit == "hours":
                return delta.days * 24
            elif unit == "minutes":
                return delta.days * 24 * 60
        except ValueError:
            return None

    def convert_to_words(self, unit: Literal["days", "hours", "minutes"] = "minutes") -> str:
        value = self._get_date_difference(unit)
        if value is None:
            raise ValueError(f"Invalid date for {unit} calculation!")
        return f"{self.p.number_to_words(value, andword='').capitalize()} {unit}"


def main():
    try:
        birth_date = input("Date of Birth: ")
        converter = DateConverter(birth_date)
        print(converter.convert_to_words("minutes"))
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()