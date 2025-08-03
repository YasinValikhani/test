import requests
import json

# url = 'https://httpbin.org/get'

# try:
#     response = requests.get(url, timeout=10)
#     print("Statuse Code:", response.status_code)
#     print("Response:")
#     print(response.text)
# except requests.exceptions.SSLError as e:
#     print("خطای SSL:", e)
# except requests.exceptions.RequestException as e:
#     print("خطای درخواست:", e)

#Q2
#Q2
#Q2


# آدرس مقصد (برای تست از httpbin.org استفاده می‌کنیم)
# url = 'https://httpbin.org/post'

# داده‌هایی که می‌خواهیم به عنوان فرم ارسال کنیم
# form_data = {
#     'username': 'Yasin',
#     'password': '123456'
# }

# try:
#     # ارسال درخواست POST با داده‌های فرم
#     response = requests.post(url, data=form_data, timeout=10)

#     # چاپ کد وضعیت و پاسخ
#     print("Status Code:", response.status_code)
#     print("Response:")
#     print(response.text)

# except requests.exceptions.RequestException as e:
#     print("خطا در ارسال درخواست:", e)

#Q2
#Q2
#Q2


# url = 'https://httpbin.org/post'

# form_data = {
#     'username': 'Yasin',
#     'password': '123456'
# }
# try:
#     response = requests.post(url,data=form_data)

#     # تبدیل پاسخ به فرمت JSON (مثل دیکشنری پایتون)
#     response_json = response.json()

#     # print(response.text)
#     print("Status Code:", response.status_code)
#     print(response_json['form'])

# except requests.exceptions.RequestException as e:
#     print("خطا در ارسال درخواست:", e)    


#Q2
#Q2
#Q2


# # آدرس وب‌سایت موردنظر
# url = 'https://httpbin.org/get'

# try:
#     # ارسال درخواست GET
#     response = requests.get(url, timeout=10)

#     # بررسی کد وضعیت
#     if response.status_code == 200:
#         print("The request was successful! ✅")
#         print("Status code:", response.status_code)

#         # نمایش سرآیندهای پاسخ
#         print("Response headers:\n")
#         for key, value in response.headers.items():
#             print(f"{key}: {value}")
#     else:
#         print("The request was unsuccessful")
#         print("Status code:", response.status_code)

# except requests.exceptions.RequestException as e:
#     print("خطا در ارسال درخواست:", e)


# data = {'a':1, 'b':2, 'c':3}
# print(json.dumps(data))
# print(type(data))



# person = {"name": "Ali", "age": 30}
# json_string = json.dumps(person)
# print(type(json_string))
# # json_string = '{"name": "Ali", "age": 30}'
# # person = json.loads(json_string)

# print(json_string)

# print(type(person))
# print(person["name"])


# یک برنامه پایتون بنویسید که یک رشته JSON را از یک فایل بخواند،
#  آن را به یک شیء تبدیل کند،
# و سپس یکی از ویژگی‌های شیء را چاپ کند.


with open("D:/Python/Exchange/Exchange/data.json", "r") as file:
    json_str = file.read()

data = json.loads(json_str)

print('NAME:',data["name"])

