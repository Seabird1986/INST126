import urllib.request as urlr
import urllib.parse as url
import urllib.error as urle
import json
import os

def phone_reply(call_var):
    Senator_Info = {}
    House_Info = {}

    entries_count = 0
    rep_number = 1

def email_reply(call_var):

    entries_count = 0
    rep_number = 1
    Senator_Info = {}
    House_Info = {}

def website_reply(call_var):
    entries_count = 0
    rep_number = 1
    Senator_Info = {}
    House_Info = {}

#Cam: Moved the functions up to the top.

global zip_code
global info_reply
zip_code = 0
info_reply = 4


begin = input("Type begin to start program: ")

if begin.lower() == 'begin' or begin.lower() == 'begin ':
    zip_code = input("Welcome to PollText! Reply with your 5-digit zip code to recieve phone number, email or website of your Senate Representative.")

    while int(info_reply) > 3:
        info_reply = input("Reply with the info you would like to receive: 1. Phone 2. Email 3. Website")
        try:
            int(info_reply) <= 3
            int(info_reply) > 0
        except:
            print("Please enter a valid input.")
else:
    print('Sorry, that was not a valid input message.')
    exit()


serviceurl = 'https://www.googleapis.com/civicinfo/v2/representatives?address=' + str(zip_code) + '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'

address = serviceurl
print('Retrieving', address)
json_df = urlr.urlopen(address).read().decode('utf-8')
print('Retrieved', len(json_df), 'characters')
info = json.loads(json_df)
print('Entry count:', len(info))

global Senate_reps
global House_reps

Senate_reps = {}
House_reps = {}

for item in info['offices']:  # create a list of the Official Indexes of Senate/House reps to pull info from
    if 'Senate' in item['name']:
        Senate_reps = item['officialIndices']
    if 'Representatives' in item['name']:
         House_reps = item['officialIndices']

#for item in info['offices']: Cam: Only commented this out in case we need to put it back. But I took the 2 lines above and condensed it into one for loop.
    

#global Senator_Info
#global House_Info Cam: Just commented this out in case we need it. It ws repeated.

entries_count = 0
rep_number = 1

while entries_count < len(info['officials']):
    for item in info['officials']:
        if entries_count in Senate_reps:
            Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
            Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
            rep_number += 1
        entries_count += 1
        if entries_count in House_reps:
            House_Info.update({'House Representative ' + str(rep_number): item['name']})
            House_Info.update({'House Representative ' + str(rep_number) + ' phone': item['phones']})
            rep_number += 1
        entries_count += 1

#while entries_count < len(info['officials']):
#    for item in info['officials']: Cam: Just commented this out in case we need to put it back.
        
    print(Senator_Info)
    print(House_Info)

entries_count = 0
rep_number = 1

while entries_count < len(info['officials']):
    for item in info['officials']:
        if entries_count in Senate_reps:
            Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
            Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
            rep_number += 1
        entries_count += 1
        if entries_count in House_reps:
            House_Info.update({'House Representative ' + str(rep_number): item['name']})
            House_Info.update({'House Representative ' + str(rep_number) + ' website': item['urls']})
            rep_number += 1
        entries_count += 1

#while entries_count < len(info['officials']):
    #for item in info['officials']: Cam: Just commented this out in case we need it.
            
    print(House_Info)
    print(Senator_Info)

# Cam: Commented out this region just because it looked to be repeated. Might need it in the future.
##    while entries_count < len(info['officials']):
##        for item in info['officials']:
##            if entries_count in Senate_reps:
##                Senator_Info.update({'Senate Representative ' + str(rep_number): item['name']})
##                Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
##                rep_number += 1
##            entries_count += 1
##
##    entries_count = 0
##    rep_number = 1
##
##    while entries_count < len(info['officials']):
##        for item in info['officials']:
##            if entries_count in House_reps:
##                House_Info.update({'House Representative ' + str(rep_number): item['name']})
##                House_Info.update({'House Representative ' + str(rep_number) + ' website': item['urls']})
##                rep_number += 1
##            entries_count += 1
##
##    print(House_Info)
##    print(Senator_Info)

if info_reply == 1:
    phone_reply(info_reply)
elif info_reply == 2:
    email_reply(info_reply)
elif info_reply == 3:
    website_reply(info_reply)
