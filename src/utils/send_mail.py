import smtplib
import email.message
from datetime import datetime
from email_body import body

server = smtplib.SMTP('smtp.gmail.com:587')  
msg = email.message.Message()
msg['Subject'] = "Cotação do Arroba do Boi"
  
# Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
  # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
# Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
# Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
msg['From'] = 'boi.gordo.newsletter@gmail.com'
msg['To'] = 'felipe.011.ms@gmail.com'
password = "Boi12345"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(body)
  
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
# Login Credentials for sending the mail
# s.login(msg['From'], password)
# s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

f = open('helloworld.html','w')

f.write(body)
f.close()

# now = datetime.now()
# print('Email sent at', now)