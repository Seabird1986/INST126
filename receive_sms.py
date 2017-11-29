#testing environment
import os
from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])


def sms_reply():
    r = MessagingResponse()
    body = request.values.get('Body', None)
    if body == 'Begin' or body == "begin" or body == 'Begin ':
        r.message("Welcome to PollText! Enter your 5-digit zip code")
        if len(body) != 5:
            r.message("Please try again, send your 5-digit zipcode")
    elif len(body) == 5:
        r.message('Enter the information you would like to retrieve')
        r.message('1. Polling Place. 2. State Senator 3. Election day')

    elif body == "End" or body == "end":
        r.message('You will no longer recieve texts from PollText')
    else:
        r.message('Sorry, that was not a valid input message.')
    return str(r)


if __name__ == "__main__":
    app.run(debug=True)
