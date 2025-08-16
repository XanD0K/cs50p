months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

month_day = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def main():
    month, day, year = get_date()
    print(f"{year}-{month:02}-{day:02}")


def get_date():
    while True:
        date = input("Date: ").strip()
        try:
            # Check date in "MM/DD/YYYY" format
            if "/" in date:
                month, day, year = map(int, date.split("/"))
            # Check date in "Month DD, YYYY" format
            else:
                month_text, day_year = date.split(" ", 1)
                day, year = day_year.split(", ")
                month = int(months[month_text.title()])
                day = int(day)
                year = int(year)
            # Validate month, day, and year
            if not(1 <= month <= 12 and 1 <= day <= month_day[month] and len(str(year)) == 4 and year > 0):
                print("Invalid date!")
                continue
            return month, day, year
        except ValueError:
            print("Invalid format. Use 'MM/DD/YYYY' or 'Month DD, YYYY'")
            continue
        except KeyError:
            print("Invalid month!")
            continue


if __name__ == "__main__":
    main()


# TODO: try with regex
# TODO: add leap year logic