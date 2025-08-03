import requests
from config import url
import json
import os 


# def get_rates():
#     response = requests.get(url)
#     data = response.json()

#     print('Exchange rate:\n')
#     print(response.text)

#     for currency, rate in data["rates"].items():
#         print (f"{currency}: {rate}")

#     print("Type of data['rates']:", type(data))

# def archive(filename, rates):
    
#     with open(f'archive/{filename}.json', 'w') as f:
#         f.write(json.dump(rates))

   
# if __name__ == '__main__':
#     data = get_rates()
#     archive(data['timestamp'],data['filename'])

# ;;;
# ;;;
# ;;;


# def get_rates():
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Request failed with status code:", response.status_code)
#         return None

# if __name__ == '__main__':
#     data = get_rates()
    
#     if "rates" in data:
#         target_currencies = ["USD", "EUR", "JPY", "IRR"]  # ارزهای مورد نظر

#         print("\nSelected Exchange Rates:\n")
#         for currency in target_currencies:
#             rate = data["rates"].get(currency)
#             if rate:
#                 print(f"{currency}: {rate}")
#             else:
#                 print(f"{currency}: ❌ Not found in response")

import requests
import json
import os 


from config import url,rules
from mail import send_smtp_email

def get_rates():
    response = requests.get(url)
    data = response.json()

    print('Exchange rate:\n')
    print(json.dumps(data, indent=2))  # چاپ مرتب

    # for currency, rate in data["rates"].items():
    #     print(f"{currency}: {rate}")

    return data  # 🔁 مهم: برگردوندن داده برای استفاده در جای دیگه

def archive(filename, rates):
# اگه فولدر archive وجود نداشته باشه، بساز
    os.makedirs('archive', exist_ok=True)
    # ذخیره در فایل
    with open(f'archive/{filename}.json', 'w') as f:
        json.dump(rates, f, indent=2)

def send_mail(timestamp, rates):

    subject = f'{timestamp} rates'

    if rules['preferred'] is not None:
        tmp = dict()
        for exc in rules['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)   

    send_smtp_email(subject, text)

if __name__ == "__main__":
    res = get_rates()

    if rules['archive']:
        archive(res['timestamp'], res['rates'])

    if rules['send_mail']:
        send_mail(res['timestamp'], res['rates'])

