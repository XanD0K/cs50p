# My API key: 9803015b4974f88a131231e613be712162299fe575eec7e432f7f3c6dc05fe2a

import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")
    elif not sys.argv[1].isdigit():
        sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")
    elif not sys.argv[1] >= 0:
        sys.exit("Provide a positive number! Usage: python bitcoin.py <positive_number>")
    bitcoin = sys.argv[1]

    try:
        float(bitcoin)   
        

    except requests.RequestException:

if __name__ == "__main__":
    main()