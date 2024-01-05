import smtplib
from email.mime.text import MIMEText
msg = MIMEText("EUR went up")
msg['Subject'] = "EUR went up"
msg['From'] = "joe@foxjazz.net"
msg['To'] = "mail@foxjazz.net"
server = smtplib.SMTP('smtp.ionos.com', 587)  # Replace with your email server's details
server.starttls()
server.login("send@foxjazz.net", "TheStruggle88**99((00))")  # Replace with your email credentials
server.sendmail(msg['From'], msg['To'], msg.as_string())
