import smtplib
from email.mime.text import MIMEText

correo_origen = ***************
contraseña = *************


msg = MIMEText("MENSAJE")
msg['Subject'] = 'ASUNTO'
msg['From'] = correo_origen
destinatario = correo destino

server = smtplib.SMTP('Servidor de Corre')
server.starttls()
server.login(correo_origen,contraseña)
server.sendmail(correo_origen,destinatario,msg.as_string())

print("Su Email ha sido enviado.")

server.quit()
