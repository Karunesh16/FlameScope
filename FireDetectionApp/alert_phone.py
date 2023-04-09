from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import datetime


accountSID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
authToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(accountSID,authToken)

twiml = VoiceResponse()
twiml.say('Fire Warning. Attention Customer, Fire Alarm Triggered at location of your home address.')

def call_alert():
    client.calls.create(
        from_='xxxxxxxxxxxx',
        to='xxxxxxxxxxxxx',
        twiml=str(twiml),
    )
    client.messages.create(
        from_='xxxxxxxxxxxxxx',
        to='xxxxxxxxxxx',
        body=f""" Fire Detected,Location : KJSIT, Ayurvihar Sion, Mumbai,Date/Time: {datetime.datetime.now()} """,
    )
    
if __name__ == '__main__':
    call_alert()
