import smtplib
import ssl
import os


def email_send(message):
    host = 'smtp.gmail.com'
    port = 465

    sender = 'mahmoudchoumar@ieu.edu.ua'
    password = os.getenv("PASSWORD")

    receiver = 'mahmoudchoumar@ieu.edu.ua'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
