import requests
import sys
import json

def main():
    apiKey="3aa5c92cb7fad3a29b5b281af908a1d25452db8a10f2a61f75f1d6178e768d55"
    if not len(sys.argv)==2:
        sys.exit("Missing command-line argument  ")
    elif validate_input():
        sys.exit("Command-line argument is not a number")
    else:
        input=float(sys.argv[1])

    try:
        r = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={apiKey}")
        response = r.json()
        amount=input* float(response["data"]["priceUsd"])
        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit("Code fatt gaya")


def validate_input():
    try:
        float(sys.argv[1])
        return False
    except:
        return True

if __name__ == "__main__":
    main()
