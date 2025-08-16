# Demonstrates pip-installed package
# Needs 'pip install cowsay'

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])