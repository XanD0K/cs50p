# Uses command-line argument to take user's input
# When controlling programs through command line, it's common to provide switches/flashes


import sys


if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows7.py [-n NUMBER]")