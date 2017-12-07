import urllib.request as urlr
import urllib.parse as url
import urllib.error as urle
import json
import os
from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
#   python /Users/cricket/Documents/GitHub/INST126/Twilio_format.py
#sunlightfoundation.com check for internships


app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])


def sms_reply():
    r = MessagingResponse()
    body = request.values.get('Body', None)

    if body.strip().lower() == "begin":
       r.message("Welcome to PollText! Text 'Phone Number XXXXX', 'Website XXXXX', or 'Address XXXXX' Replacing X's with 5-Digit ZipCode")        
    elif len(body) == 18:
        #Phone Number XXXXX' 18 char
        body_zip = body[13:]
        s1 = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
        zc = str(body_zip)
        s3 = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
        serviceurl = s1+zc+s3
        address = serviceurl
        #r.message(str(serviceurl))
        print('Retrieving', address)
        json_df = urlr.urlopen(address).read().decode('utf-8')
        print('Retrieved', len(json_df), 'characters')
        info = json.loads(json_df)
        print('Entry count:', len(info))
        Senate_reps = {}
        for item in info['offices']: #create a list of the Official Indexes of Senate/House reps to pull info from
            if 'Senate' in item['name']:
                Senate_reps = item['officialIndices']
        entries_count = 0
        rep_number = 1
        Senator_Info = {}
        while entries_count < len(info['officials']):
            for item in info['officials']:
                if entries_count in Senate_reps:
                    Senator_Info.update({item['name']:item['phones']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' address': item['address']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
                    rep_number += 1
                entries_count += 1
        entries_count = 0
        rep_number = 1
        r.message(str(Senator_Info))
    elif len(body) == 13:
        #'Website XXXXX' 13 char
        body_zip = body[8:]
        s1 = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
        zc = str(body_zip)
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
        entries_count = 0
        rep_number = 1
        Senator_Info = {}
        while entries_count < len(info['officials']):
            for item in info['officials']:
                if entries_count in Senate_reps:
                    Senator_Info.update({item['name']:item['urls']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' address': item['address']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' emails': item['urls']})
                    rep_number += 1
                entries_count += 1
        entries_count = 0
        rep_number = 1
        r.message(str(Senator_Info))
    elif len(body) == 13:
        #'Address XXXXX' 13 char
        body_zip = body[8:]
        s1 = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
        zc = str(body_zip)
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
        entries_count = 0
        rep_number = 1
        Senator_Info = {}
        while entries_count < len(info['officials']):
            for item in info['officials']:
                if entries_count in Senate_reps:
                    Senator_Info.update({item['name']:item['address']})

                    #Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' address': item['address']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
                    #Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
                    rep_number += 1
                entries_count += 1
        entries_count = 0
        rep_number = 1


        
        r.message(str(Senator_Info))
    else:
        r.message("Broken, Try Again")
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)



#How we will do some error checking and just extract their zip, meaning we can eliminate
# the current part where we check for lenght.     
'''
body = input('enter phone: ')


import re
if body.startswith('phone') or if body.startswith('phone'):
    a = re.findall(r'\d+', 'Phone Number 20904')
    c = str(list(a))
    d = c[2:-2]
    e = "google.com/address="+d
    print(e)




''''

