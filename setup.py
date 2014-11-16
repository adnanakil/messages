from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC290582373b22d8217957a62974d75ce8"
auth_token  = "1037caa6e137bc8d996a98c0acb5c025"
client = TwilioRestClient(account_sid, auth_token)
 

@app.route("/send")
def send_message():
	message = client.messages.create(body="HELLO?! IS ANYBODY THERE?!",
    to="+12017570419",
    from_="+14158814524")
	print message.sid
	return message.sid


 
if __name__ == "__main__":
    app.run(debug=True)


