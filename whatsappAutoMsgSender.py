from twilio.rest import Client

account_sid = 'ACf7c5179e77b12874197d439accf03a8a'
auth_token = '6f9ed3d7b5105209fd0d96b2ce003f9c'
client = Client(account_sid, auth_token)

def sendMsg():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Hi Raghav, I miss you so much 💕💖💞',
                                  to='whatsapp:+918630689227'
                              )

    print(message.sid)
