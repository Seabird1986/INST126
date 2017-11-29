# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "" #get our api key from the google drive. 
auth_token = ""
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+13012049407",#you need to change this number to urs
    from_="+12407861570",
    body="Welcome to PollText, Reply 'Begin' to Start!")
