"""
                      .-.
                     ()I()
                "==.__:-:__.=="
               "==.__/~|~\__.=="
               "==._(  Y  )_.=="
    .-'~~""~=--...,__\/|\/__,...--=~""~~'-.
   (               ..=\=/=..               )
    `'-.        ,.-"`;/=\ ;"-.,_        .-'`
        `~"-=-~` .-~` |=| `~-. `~-=-"~`
             .-~`    /|=|\    `~-.
          .~`       / |=| \       `~.
      .-~`        .'  |=|  `.        `~-.
    (`     _,.-="`    |=|    `"=-.,_     `)
     `~"~"`           |=|           `"~"~`
                      |=|
                      |=|
                      |=|
                      /=\\

------------------------------------------------
Author: Leonidas Reppas
"""

from twilio.rest import Client
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from src.watson import WatsonLang

import json

account_sid = "ACb7774b0b683f617feea02e6d667beb3c"
auth_token = "97d69f73e6d9b03a9ba17b895d7474b5"
client = Client(account_sid, auth_token)

# The session object makes use of a secret key.
SECRET_KEY = '97d69f73e6d9b03a9ba17b895d7474b5'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "Angelos": "+447484330666",
    "Leo": "+447519451663",
    "Geo": "+447598734567",
    "Andy": "+447519451663",
    "Jordan": "+447588434313"
}

state = {}

def send_sms(to_num, text):
    message = client.messages \
                .create(
                     body=text,
                     from_='+441297533050',
                     to=to_num
                 )

@app.route("/sms", methods=['GET', 'POST'])
def hello():
    participants = state.get('participants', [])

    from_number = request.values.get('From') 
    text = request.values.get('Body')

    watch = WatsonLang()
    emotions = watch.analyze_emotion(text)

    if text.startswith("start conversation"):
        to_num = callers.get(text.split()[3])
        if not to_num:
            raise
    
        state['participants'] = [to_num, from_number]

    elif text.startswith("end conversation"):
        state['participants'] = []

    else:
        if not state['participants']:
            raise
        if from_number == state['participants'][0]:
            to_number = state['participants'][1]
        else:
            to_number = state['participants'][0]
        send_sms(to_number, text)
    print(state)
    

    # Build our reply
    message = json.dumps(emotions)

    # Put it in a TwiML response
    resp = MessagingResponse()
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)