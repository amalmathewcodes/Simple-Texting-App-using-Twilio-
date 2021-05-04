from twilio.rest import Client

from credentials import account_sid , auth_token ,my_cell ,my_twilio


client =Client(account_sid , auth_token)


my_msg = 'For the Google Ceo , You are the best in the world'


message = client.messages.create(to=my_cell,from_ = my_twilio , body = my_msg)
