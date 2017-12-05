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
    if body == 'SenPhone':
        r.message("Welcome to PollText! Reply with Zip for Senators Phone Num's.")
    try: 
        if len(body) == 5:
            url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
            z_c = str(body)
            key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
            serviceurl = url+z_c+key
            address = serviceurl
            r.message(str(serviceurl + "Phone"))
        else:
            r.message("SenPhone, SenWeb, SenEmail")
            
    
    elif body == 'SenWeb':
        r.message("Welcome to PollText! Reply with Zip for Senators Website.")
        try:
            if len(body) == 5:
                url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
                z_c = str(body)
                key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
                serviceurl = url+z_c+key
                address = serviceurl
                r.message(str(serviceurl + "Website"))
            else:
                r.message("SenPhone, SenWeb, SenEmail")
                

    elif body == "SenEmail":
        r.message("Welcome to PollText! Reply with Zip for Senators Email's.")
        try:
            if len(body) == 5:
                url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
                z_c = str(body)
                key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
                serviceurl = url+z_c+key
                address = serviceurl
                r.message(str(serviceurl + "Email"))
            
        except:
            r.message('Sorry, that was not a valid input message.')

    return str(r)

if __name__ == "__main__":
    app.run(debug=True)






