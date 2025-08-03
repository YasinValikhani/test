import os

BASE_PATH = 'http://data.fixer.io/api/latest?access_key='
API_KEY = 'fbe722d70c2bd3a2842e97c0b2c56671'  # بهتره از os.environ.get استفاده کنی برای امنیت

url = BASE_PATH + API_KEY
print("✅ config loaded, url =", url)

EMAIL_RECEIVER = "A Test User <to@example.com>"

rules = {
    'archive': True,
    'send_mail': True,
    'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD', 'AED']  # یا None بذار اگه همه ارزها رو می‌خوای
}
