from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from src.watson import WatsonLang

import json

# The session object makes use of a secret key.
SECRET_KEY = '97d69f73e6d9b03a9ba17b895d7474b5'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+447484330666": "Angelos",
    "+12349013030": "Finn",
    "+12348134522": "Chewy",
}


@app.route("/sms", methods=['GET', 'POST'])
def hello():
    """Respond with the number of text messages sent between two parties."""
    # Increment the counter
    counter = session.get('counter', 0)
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')
    text = request.values.get('Body')
    watch = WatsonLang()
    emotions = watch.analyze_emotion(text)
    
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"

    # Build our reply
    message = json.dumps(emotions)

    # Put it in a TwiML response
    resp = MessagingResponse()
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)