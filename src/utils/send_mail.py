import smtplib
import email.message
from datetime import datetime
from email_body import body
from decouple import config # use .env to sensitive informations

server = smtplib.SMTP('smtp.gmail.com:587')  
msg = email.message.Message()
msg['Subject'] = "Cotação do Arroba do Boi"
  
# Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
# Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
# Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
# Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha

#Configure your .env to use the variables bellow
msg['From'] = config('mail_from')
msg['To'] = config('mail_to')
password = config('mail_password')

msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)
  
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
# Login Credentials for sending the mail
# s.login(msg['From'], password)
# s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))



# now = datetime.now()
# print('Email sent at', now)