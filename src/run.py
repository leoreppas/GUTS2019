"""
                      .-.
                     ()I()
                "==.__:-:__.=="
               "==.__/~|~\__.=="
              "==._( . Y . )_.=="
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
import pickle

import json

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

# The session object makes use of a secret key.
SECRET_KEY = ''
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "Angelos": "",
    "Leo": "",
    "Geo": "",
    "Andy": "",
    "Jordan": ""
}

contacts = {"Jordan": {"number": "", "relation": "friend"}}

state = {}

def send_sms(to_num, text):
    message = client.messages \
                .create(
                     body=text,
                     from_='',
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
        state["callee"] = text.split()[3]
        to_num = contacts.get(state["callee"]).get('number')
        if not to_num:
            raise
    
        state['participants'] = [to_num, from_number]

    elif text.startswith("end conversation"):
        state['participants'] = []
        state["callee"] = ''
        
    elif text.startswith("add contact"):
        text = text[len('add contact'):]
        text = text.split()
        for contact in list(contacts):
            if from_number == contacts[contact]["number"]:
                name = contact
        contacts[text[0]] = {"number":text[1], "relation": text[2]}
    
    else:
        if not state['participants']:
            raise
        if from_number == state['participants'][0]:
            to_number = state['participants'][1]
        else:
            to_number = state['participants'][0]

        if to_number == contacts[state["callee"]]['number']:
            # Analyze text and decide to indicate if the person should send or no.
            watch = WatsonLang()
            emotions = watch.analyze_emotion(text)
            # Load in 4 models
            models = {
                'ex': 'exes_model.sav',
                'friend': 'friends_model.sav',
                'parent': 'parents_model.sav',
                'colleague': 'colleague_model.sav'
            }
            model_file = models[contacts[state["callee"]]['relation']]
            model = pickle.load(open(model_file,'rb'))
            emo = [list(emotions.values())]
            answer = model.predict(emo)
            print(answer)
            if list(answer)[0] == '1':
                send_sms(to_number, text)
            else:
                send_sms(from_number, "Your answer was deemed unworthy")
        else:
            send_sms(to_number, text)
    print(state)
    print(contacts)
    

    # Build our reply
    message = json.dumps(emotions)

    # Put it in a TwiML response
    resp = MessagingResponse()
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
