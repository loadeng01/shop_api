from twilio.rest import Client
from decouple import config


def sending_sms(text='You get it', receiver='+996703321438'):
    if receiver[0] != '+':
        receiver = '+' + receiver

    try:
        account_sid = config('SID')
        auth_token = config('AUTH_TOKEN')
        client = Client(account_sid, auth_token)
    except:
        return 'Something wrong with create Twilio Client'

    try:
        message = client.messages.create(
            body=text,
            from_='+19196480549',
            to=receiver
        )
        return 'Message was successfully sent'
    except Exception as e:
        print(e)
        return 'Something wrong'




