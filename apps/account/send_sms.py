from twilio.rest import Client
from decouple import config


def send_activation_sms(phone_number, activation_code):
    message = f'Your activation code: {activation_code}'
    account_sid = config('SID')
    auth_token = config('AUTH_TOKEN')
    twilio_sender_phone = config('TWILIO_SENDER_PHONE')

    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=twilio_sender_phone, to=phone_number)







# def sending_sms(text='You get it', receiver='+996703321438'):
#     if receiver[0] != '+':
#         receiver = '+' + receiver
#
#     try:
#         account_sid = config('SID')
#         auth_token = config('AUTH_TOKEN')
#         twilio_sender_phone = config('TWILIO_SENDER_PHONE')
#         client = Client(account_sid, auth_token)
#     except:
#         return 'Something wrong with create Twilio Client'
#
#     try:
#         message = client.messages.create(
#             body=text,
#             from_=twilio_sender_phone,
#             to=receiver
#         )
#         return 'Message was successfully sent'
#     except Exception as e:
#         print(e)
#         return 'Something wrong'




