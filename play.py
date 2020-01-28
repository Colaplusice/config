# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc6765fbe1c9b50b9faff5077fa22dade'
auth_token = '1e43c1d1e9d3231ab9e3eec3a56a6a29'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hey, ugly MotherFucker, this is the beginning of the Revenge",
                     from_='+12029911798',
                     to='+17367293091'
                 )

print(message.sid)
