# My API key: 9803015b4974f88a131231e613be712162299fe575eec7e432f7f3c6dc05fe2a

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")
    elif not float(sys.argv[1]) >= 0:
        sys.exit("Provide a positive number! Usage: python bitcoin.py <positive_number>")
    bitcoin = float(sys.argv[1])

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9803015b4974f88a131231e613be712162299fe575eec7e432f7f3c6dc05fe2a"
        )   
    except requests.RequestException:
        print("Could't access that information!")

    object = response.json()
    total_price = bitcoin * float(object["data"]["priceUsd"])
    print(f"${total_price:,.4f}")

if __name__ == "__main__":
    main()