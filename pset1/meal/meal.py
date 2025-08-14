def main():
    time = input("What time is it? ")
    
    try:
        current_time = convert(time)

        if 7.0 <= current_time <= 8.0:
            print("It's breakfast time")
        elif 12.0 <= current_time <= 13.0:
            print("It's lunch time")
        elif 18.0 <= current_time <= 19.0:
            print("It's dinner time")
        else:
            print("It's not meal time")
    
    except ValueError:
        print("Invalid time format! Use HH:MM")


def convert(time):
    if ":" not in time:
        raise ValueError("Time must contain ':'")
    hours, minutes = time.split(":")

    # Validade hours and minutes
    hours = float(hours)
    minutes = float(minutes)
    if not (0 <= hours < 24):
        raise ValueError("Hours must be between 0 and 23.")
    if not (0 <= minutes < 60):
        raise ValueError("Minutes must be between 0 and 59")

    return hours + minutes / 60


if __name__ == "__main__":
    main()

# TODO: handle AM/PM format