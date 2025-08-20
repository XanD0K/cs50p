from pathlib import Path

import csv
import sys

def main():
    # Check for 3 command-line arguments and for a .csv file
    if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Usage: python scourgify.py before.csv <filename.csv>")

    # Check if file exists (and dismiss later check for FileNotFoundError)
    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        sys.exit(f"File {sys.argv[1]} does not exist!")

    try:
        with input_path.open() as input_file:
            reader = csv.DictReader(input_file)

            output_path = Path(sys.argv[2])
            with output_path.open("w", newline="") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                
                # Segregate 'name' column into 'last' and 'first' variables
                for row in reader:
                    last, first = row["name"].split(", ")            
                    writer.writerow({"first": first, "last": last, "house": row["house"]})
               
    except (PermissionError, csv.Error) as e:
        sys.exit(f"Error reading files: {e}")          


if __name__ == "__main__":
    main()