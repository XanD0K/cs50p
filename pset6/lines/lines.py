from pathlib import Path
import os
import sys

def main():
    # Checks for 2 command-line arguments and for python files
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Incorrect usage! Usage: 'python files.py <filename.py>'")
    
    # Check if file exists
    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        sys.exit(f" File {sys.argv[1]} does not exist")
    # Could also check for file's exisntece with 'os.path.exists(sys.argv[1])'

    # Keep track of number of lines
    line_count = 0
    try:
        with file_path.open() as file: # If using os → with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                # Exclude from count comments and whitespace-lines
                if line and not line.startswith("#"):
                    line_count += 1
    except FileNotFoundError:
        sys.exit(f"Couldn't open file {sys.argv[1]}")
    except PermissionError:
        sys.exit(f"Couldn't read file {sys.argv[1]}")
    
    print(line_count)


if __name__ == "__main__":
    main()