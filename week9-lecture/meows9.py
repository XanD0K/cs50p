# Adds description, help
# It's conventional to run a program with the special ragument -h or --help
# It will show usage information


import argparse

# Adds description to the program
parser = argparse.ArgumentParser(description="Meow like a cat")
# Adds description to the -n flag
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
