# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC290582373b22d8217957a62974d75ce8"
auth_token  = "1037caa6e137bc8d996a98c0acb5c025"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+12017570419", from_="+14158814524",
                                     body="Hello there!")
