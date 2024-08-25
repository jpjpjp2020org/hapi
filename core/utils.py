from twilio.rest import Client
from django.conf import settings

def send_twilio_message(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=to,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=message
    )
    print(f"Sent message: {message.sid}")
