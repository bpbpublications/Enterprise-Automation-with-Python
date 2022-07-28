from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Replace with Account SID"
# Your Auth Token from twilio.com/console
auth_token  = "Replace with auth token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="Replace with number to send",
    from_="+18484208847",
    body="Automation bot message!")

print(message.sid)
