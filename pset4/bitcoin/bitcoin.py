import requests
import sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    num = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        #
        #
        pass
    else:
        output = response.json()
        price = float(output["bpi"]["USD"]["rate_float"])

        result = num * price
        print("${:,.4f}".format(result))
