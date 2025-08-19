from pathlib import Path
from tabulate import tabulate

import csv
import sys


def main():
    pizza = []

    # Checks for 2 command-line arguments and for .csv file
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <filename.csv>")

    # Check if file exists
    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        sys.exit(f"File {sys.argv[1]} does not exist")

    try:
        with file_path.open() as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza.append(row)

    # Already checking file before this try-except block. Don't need 'FileNotFoundError' exception
    except (PermissionError, csv.Error) as e:
        sys.exit(f"Error reading file {sys.argv[1]}: {e} ")

    print(tabulate(pizza, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()