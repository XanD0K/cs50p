# Demonstrates own module

import sys

from sayings2 import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])