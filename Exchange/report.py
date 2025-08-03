import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 1. ساخت گزارش ساده
report_text = "گزارش روزانه:\n- فروش: 500 دلار\n- سود: 120 دلار\n- مشتریان: 25 نفر"

# 2. ذخیره در فایل متنی
filename = "report.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(report_text)

# 3. تنظیمات ایمیل
sender_email = "Private Person <from@example.com>"
receiver_email = "A Test User <to@example.com>"
subject = "گزارش روزانه"

# 4. ساخت بدنه ایمیل
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# 5. متن داخل ایمیل
body = "سلام،\nگزارش روزانه پیوست شده است."
message.attach(MIMEText(body, "plain"))

# 6. اضافه کردن فایل متنی به ایمیل به عنوان پیوست
with open(filename, "rb") as f:
    attachment = MIMEApplication(f.read(), _subtype="txt")
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(attachment)

# 7. اطلاعات Mailtrap (یا سرور SMTP دیگر)
smtp_server = "sandbox.smtp.mailtrap.io"
port = 2525
username = "ffcacb02433ffe"
password = "eb1b0ae3974b18"

# 8. ارسال ایمیل
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print(" ایمیل با پیوست ارسال شد.")



