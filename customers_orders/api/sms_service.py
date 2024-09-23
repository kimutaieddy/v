import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms(phone_numner, message):
    try:
        response=sms.send(message,[phone_numner])
        print(f"SMS sent successfully: {response}")