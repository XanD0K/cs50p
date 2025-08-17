import json
import requests
import sys


def main():
    # Ensure there is 2 command line arguments
    if len(sys.argv) != 2:
        sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")

    # Try convertion to float
    try:
        bitcoin = float(sys.argv[1])
        # Ensure user enter a positive value
        if bitcoin < 0:
            sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")
    except ValueError:
        sys.exit("Incorrect usage. Usage: python bitcoin.py <positive_number>")

    # Try getting an API response
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9803015b4974f88a131231e613be712162299fe575eec7e432f7f3c6dc05fe2a"
        )

        # Storing json response in an object
        data = response.json()
        if "data" not in data or "priceUsd" not in data["data"]:
            sys.exit("Invalid API response")

        # Calculate price
        total_price = bitcoin * float(data["data"]["priceUsd"])

        print(f"${total_price:,.4f}")

    except requests.RequestException:
        sys.exit("Could't get an API response!")

if __name__ == "__main__":
    main()
