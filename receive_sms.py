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
    begin = request.values.get('Body', None)
    zipcode = request.values.get('Body', None)
    demand = request.values.get('Body', None)
    if begin == 'Begin' or begin == "begin" or begin == 'Begin ':
        r.message("Welcome to PollText! Reply with your 5-digit zip code to recieve phone number, email or website of your Senate Representative. ")
        if len(zipcode) != 5:
            r.message("Please try again, send your 5-digit zipcode")
    elif len(zipcode) == 5:
        s1 = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
        zc = str(zipcode)
        s3 = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
        serviceurl = s1+zc+s3
        address = serviceurl
        print('Retrieving', address)
        json_df = urlr.urlopen(address).read().decode('utf-8')
        print('Retrieved', len(json_df), 'characters')
        info = json.loads(json_df)
        print('Entry count:', len(info))

        Senate_reps = {}
        
        for item in info['offices']: #create a list of the Official Indexes of Senate/House reps to pull info from
            if 'Senate' in item['name']:
                Senate_reps = item['officialIndices']

        for item in info['offices']:
            if 'Representatives' in item['name']:
                House_reps = item['officialIndices']
        entries_count = 0
        rep_number = 1
        Senator_Info = {}
        House_Info = {}
        while entries_count < len(info['officials']):
            for item in info['officials']:
                if entries_count in Senate_reps:
                    Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' address': item['address']})
                    Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
                    rep_number += 1
                entries_count += 1

        entries_count = 0
        rep_number = 1
        r.message(str(Senator_Info))                
    else:
        r.message('Sorry, that was not a valid input message.')
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)



#currently using my zip code as the testbed, will worry about user input zip codes later




