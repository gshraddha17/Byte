from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC88620b526d75aff90332d5824aa89a83'
auth_token = '2471d8bfe836eafc8f7c3ba3654e295e'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to=input(),  # Phone number to call (in E.164 format)
    from_='+917704059089',  # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # URL of TwiML bin or TwiML code to execute when the call is answered
)

print(call.sid)  # Print the call SID
