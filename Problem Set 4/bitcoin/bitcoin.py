from sys import argv, exit
import requests


def main():
    if len(argv) < 2:
        exit("Missing command-line argument")
    elif len(argv) > 2:
        exit("Enter only one command-line argument")

    try:
        multiplier = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")

    bitcoin = get_bitcoin()
    print(f"${bitcoin * multiplier:,.4f}")


def get_bitcoin():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json_response = response.json()

    return json_response['bpi']['USD']['rate_float']


main()