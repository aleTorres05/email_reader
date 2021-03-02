from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create text object instance
msg = MIMEMultipart()

text = "Thank you"
# setup the parameters of the email
password = "YOUR_PASSWORD"
msg["From"] = "SENDER'S_EMAIL@EMAIL.com"
msg["To"] = "RECIVER'S_EMAIL.com"
msg["Subject"] = "SUBJECT"
# add in the text body
msg.attach(MIMEText(text, "plain"))
# create server
server = smtplib.SMTP("smtp.gmail.com: 587")
server.starttls()
# Login Credentials for sending the mail
server.login(msg["From"], password)

# send the text via the server.
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()

print("successfully sent email to %s:" % (msg["To"]))
