# To prevent overchecking, when program has multiple flags, we can use third-parties libraries
# 'argparse' handles the parsing, the analysis of command line arguments


import argparse


parser = argparse.ArgumentParser()
# Adds -n as a command line argument
parser.add_argument("-n")
# Parse the command line arguments
# It automatically imports 'sys' library
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")