import requests
import json

import sys


if len(sys.argv) != 2:
    sys.exit("Missing command line argument")
else:
    try:
        float(sys.argv[1])
    except:
        sys.exit("command line argument must be a number")


try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = float(request.json()["bpi"]["USD"]["rate"].replace(",", ""))
    cost = float(sys.argv[1]) * price
    print(f"${cost:,}")
except requests.RequestException:
    sys.exit()
