import re


def main():
    hours = input("Hours: ").strip()
    print(convert(hours))


def convert(s):
    if matches := re.search(r"^([1-9][0-2]?)(?::([0-5][0-9]))? (AM|PM) to ([1-9][0-2]?)(?::([0-5][0-9]))? (AM|PM)$", s):
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = matches.groups()

        start_hour = int(start_hour)
        end_hour = int(end_hour)

        # Validate hours
        if not (1 <= start_hour <=  12 and 1 <= end_hour <= 12):
            raise ValueError("Hours must be between 1 and 12")

        # Convert hours
        start_hour = convert_hours(start_hour, start_period)
        end_hour = convert_hours(end_hour, end_period)

        # Handle absence of minutes
        start_minute = start_minute if start_minute else "00"
        end_minute = end_minute if end_minute else "00"

        return f"{start_hour:02d}:{start_minute} to {end_hour:02d}:{end_minute}"

    raise ValueError("Invalid time format!")


def convert_hours(hour, period):
        if period == "AM":
            hour = 0 if hour == 12 else hour
        elif period == "PM":
            hour = (hour % 12) + 12
        return hour


if __name__ == "__main__":
    main()
