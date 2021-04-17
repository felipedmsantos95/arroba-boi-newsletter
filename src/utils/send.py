import smtplib, ssl

from datetime import datetime
from .email_ox.body import body
from decouple import config # use .env to sensitive informations

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configure your .env to use the variables bellow
# sender_email = config('mail_from')
# receiver_email = config('mail_to').split(',')

from_addr = config('mail_from')
password = config('mail_password')

#Workarround to hide email recipent list to user
to_addr = ''
recipients = config('mail_to').split(',')

message = MIMEMultipart("alternative")
message["Subject"] = "Cotação do Arroba do Boi"
message["From"] = from_addr
message["To"] = to_addr

# Turn these into plain/html MIMEText objects
mime = MIMEText(body, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(mime)


def email_ox():
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_addr, password)
        server.sendmail(
            from_addr, [from_addr] + recipients , message.as_string()
        )
    now = datetime.now()
    print('Email sent at', now)