import requests
from config import url


def get_rates():
    response = requests.get(url)
    data = response.json()
    print('Exchange rate:\n')
    
    for currency, rate in data["rates"].items():
        print(f"{currency}: {rate}")

if __name__ == '__main__':
    get_rates()


