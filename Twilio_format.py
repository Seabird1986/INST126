import urllib.request as urlr
import urllib.parse as url
import urllib.error as urle
import json
import os
from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])


def sms_reply():
    r = MessagingResponse()
    body = request.values.get('Body', None)
    
    while True:
        if body == 'SenPhone':
            r.message("Welcome to PollText! Reply with Zip for Senators Phone Num's.")
        try:
            if len(body) == 5:
                r.message('Phone')
                break
        except ValueError:
            r.message("SenPhone, SenWeb, SenEmail")
        else:
            pass
    
        if body == 'SenWeb':
            r.message("Welcome to PollText! Reply with Zip for Senators Website.")
        try:
            if len(body) == 5:
                r.message("Web")
                break
        except ValueError:
            r.message("SenPhone, SenWeb, SenEmail")
        else:
            break

        if body == "SenEmail":
            r.message("Welcome to PollText! Reply with Zip for Senators Email's.")
        try:
            if len(body) == 5:
                r.message('Email')
                break
        except ValueError:
            r.message("SenPhone, SenWeb, SenEmail")
        else:
            break
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)






