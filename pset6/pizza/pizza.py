from pathlib import Path
from tabulate import tabulate

import csv
import sys


def main():
    # Checks for 2 command-line arguments and for .csv file
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Usage: python pizza.py <filename.csv>")

    # Check if file exists
    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        sys.exit(f"File {sys.argv[1]} does not exist")

    try:
        with file_path.open() as file:
            reader = csv.DictReader(file)
            # Removed the list to work directly with 'reader'
            print(tabulate(reader, headers="keys", tablefmt="grid"))

    # Already checking file before this try-except block. Don't need 'FileNotFoundError' exception
    except (PermissionError, csv.Error) as e:
        sys.exit(f"Error reading file {sys.argv[1]}: {e} ")


if __name__ == "__main__":
    main()
