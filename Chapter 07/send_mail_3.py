import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = input("Type your password and press enter: ")
context = ssl.create_default_context()
sender_email = "pyemailtestautomation@gmail.com"
receiver_email = "pyemailtestautomation@gmail.com"
# Creation of the MIMEMultipart Object
message = MIMEMultipart()
message["Subject"] = "Automation Bot"
message["From"] = sender_email
message["To"] = receiver_email
# HTML message
html_message = """<html>
    <head></head>
    <body>
        <p style='color:red;'>I am automating sending of email.</p>
        <p>Automation Bot</p>
    </body>
</html>"""
# Creation of a MIMEText Part
htmlPart = MIMEText(html_message, 'html')
# Part attachment
message.attach(htmlPart)

# connecting to google SMTP Server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())





