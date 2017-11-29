import urllib.request as urlr
import urllib.parse as url
import urllib.error as urle
import json

#currently using my zip code as the testbed, will worry about user input zip codes later

serviceurl = 'https://www.googleapis.com/civicinfo/v2/representatives?address=21046&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'

address = serviceurl
print('Retrieving', address)
json_df = urlr.urlopen(address).read().decode('utf-8')
print('Retrieved', len(json_df), 'characters')
info = json.loads(json_df)
print('Entry count:', len(info))

Senate_reps = {}
House_reps = {}

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
            Senator_Info.update({'Senate Representative ' + str(rep_number) + ' address': item['address']})
            Senator_Info.update({'Senate Representative ' + str(rep_number) + ' phone': item['phones']})
            Senator_Info.update({'Senate Representative ' + str(rep_number) + ' website': item['urls']})
            rep_number += 1
        entries_count += 1

entries_count = 0
rep_number = 1

while entries_count < len(info['officials']):
    for item in info['officials']:
        if entries_count in House_reps:
            House_Info.update({'House Representative ' + str(rep_number): item['name']})
            House_Info.update({'House Representative ' + str(rep_number) + ' address': item['address']})
            House_Info.update({'House Representative ' + str(rep_number) + ' phone': item['phones']})
            House_Info.update({'House Representative ' + str(rep_number) + ' website': item['urls']})
            rep_number += 1
        entries_count += 1

print(Senator_Info)
print(House_Info)