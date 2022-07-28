import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Creates a secure SSL context
context = ssl.create_default_context()

message = """\
Subject: Hi there

I am automating sending of email."""

sender_email = "pyemailtestautomation@gmail.com"
receiver_email = "pyemailtestautomation@gmail.com"

# connecting to google SMTP Server
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

