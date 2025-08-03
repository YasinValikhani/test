import smtplib

def send_smtp_email(subject, text):
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

{text}"""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login("ffcacb02433ffe", "eb1b0ae3974b18")
        server.sendmail(sender, receiver, message)
