from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import datetime


accountSID = "ACe192f0d284a13cd8a7efc5ebb7128dec"
authToken = "4ed94f5f16fa842046e82319a93729b7"

client = Client(accountSID,authToken)

twiml = VoiceResponse()
twiml.say('Fire Warning. Attention Customer, Fire Alarm Triggered at location of your home address.')

def call_alert():
    client.calls.create(
        from_='+15674065649',
        to='+918655464747',
        twiml=str(twiml),
    )
    client.messages.create(
        from_='+15674065649',
        to='+918655464747',
        body=f""" Fire Detected,Location : KJSIT, Ayurvihar Sion, Mumbai,Date/Time: {datetime.datetime.now()} """,
    )
    
if __name__ == '__main__':
    call_alert()