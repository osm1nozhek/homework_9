import os

from celery import shared_task
from twilio.rest import Client


@shared_task
def send_messages(number):
    print("1")
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "ACec2a35c8a53e4f514808e3bfb75bb0b7"
    auth_token = os.getenv("TWILIO_TOKEN")
    print(auth_token)

    client = Client(account_sid, auth_token)
    print(client)
    message = client.messages.create(
        body="Hello from Twilio", from_="+12707166231", to=number
    )
    print(message.sid)
