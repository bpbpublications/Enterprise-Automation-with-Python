import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Creates a secure SSL context
context = ssl.create_default_context()

# connecting to google SMTP Server
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("pyemailtestautomation@gmail.com", password)
    print("Connection Establised")
