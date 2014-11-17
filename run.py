from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
 


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)


# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
#     resp = twilio.twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)


@app.route("/send")
def send_message():
  message = client.messages.create(body="HELLO?! IS ANYBODY THERE?!",
    to="+12017570419",
    from_="+14158814524")
  print message.sid
  return message.sid





# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC290582373b22d8217957a62974d75ce8"
auth_token  = "1037caa6e137bc8d996a98c0acb5c025"
client = TwilioRestClient(account_sid, auth_token)
 
# Try adding your own number to this list!
callers = {
    "+12017570419": "Curious George"
}


if __name__ == "__main__":
    app.run(debug=True)


