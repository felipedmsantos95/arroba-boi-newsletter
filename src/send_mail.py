import smtplib, ssl

from datetime import datetime
from utils.email_ox.body import body
from decouple import config # use .env to sensitive informations

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configure your .env to use the variables bellow
sender_email = config('mail_from')
receiver_email = config('mail_to')
password = config('mail_password')

message = MIMEMultipart("alternative")
message["Subject"] = "Cotação do Arroba do Boi"
message["From"] = sender_email
message["To"] = receiver_email


# Turn these into plain/html MIMEText objects
mime = MIMEText(body, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(mime)


def send_email():
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    now = datetime.now()
    print('Email sent at', now)

send_email()