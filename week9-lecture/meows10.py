# Adds default, type; removes int()


import argparse


parser = argparse.ArgumentParser(description="Meow like a cat")
# Adds default value, in case user doesn't input any value
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

# Since I told 'parser' that the value is an 'int', I don't need to manually do the conversion
# If user doesn't cooperate (e.g. inputs a str) it will also generate a message handling the exception error
for _ in range(args.n):
    print("meow")
