# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC97d26327e6d81f889e210134cbabf940"
auth_token = "9b81a6156300bfcfc21ba043d22f24a5"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+13012049407",#you need to change this number to urs
    from_="+12407861570",
    body="Welcome to PollText, Reply 'Begin' to Start!")
