import time
import requests

# List of addresses to monitor (example)
ADDRESSES = [
    "0xAbC1234...def",
    "0xDef5678...abc"
]

# URL of blockchain explorer API (example)
API_URL = "https://api.etherscan.io/api"

API_KEY = "YourApiKeyToken"

def check_address(address):
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            txs = data["result"]
            # Check if recent transaction is suspicious
            if txs:
                latest_tx = txs[0]
                print(f"Recent TX for {address}: {latest_tx['hash']}")
                # Add your suspicious logic here
        else:
            print(f"No transactions found for {address}")
    else:
        print(f"Failed to fetch data for {address}")

def main():
    while True:
        for addr in ADDRESSES:
            check_address(addr)
        print("Waiting 60 seconds before next check...")
        time.sleep(60)

if __name__ == "__main__":
    main()
