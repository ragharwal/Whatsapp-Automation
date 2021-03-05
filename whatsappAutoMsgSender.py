from twilio.rest import Client

account_sid = '<account_sid>'
auth_token = '<auth_token>'
client = Client(account_sid, auth_token)

def sendMsg():
    message = client.messages.create(
                                  from_='whatsapp:<sender>',
                                  body='How are you doing?',
                                  to='whatsapp:<receiver>'
                              )

    print(message.sid)
