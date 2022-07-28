import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

password = input("Type your password and press enter: ")
context = ssl.create_default_context()
sender_email = "pyemailtestautomation@gmail.com"
receiver_email = "pyemailtestautomation@gmail.com"
message = MIMEMultipart()
message["Subject"] = "Automation Bot"
message["From"] = sender_email
message["To"] = receiver_email
# File name located in same directory as this script
filename = "large_file.pdf"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
message.attach(part)

# connecting to google SMTP Server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())





