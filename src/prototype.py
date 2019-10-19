from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb7774b0b683f617feea02e6d667beb3c'
auth_token = '97d69f73e6d9b03a9ba17b895d7474b5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15024132587',
                     to='+447484330666'
                 )

print(message.sid)