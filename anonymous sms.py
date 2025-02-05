from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = "your_account_sid"
AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE = "your_twilio_phone_number"
TARGET_PHONE = "recipient_phone_number"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="This is an anonymous message!",
    from_=TWILIO_PHONE,
    to=TARGET_PHONE
)

print(f"Message sent! SID: {message.sid}")
import requests

url = "https://textbelt.com/text"
data = {
    "phone": "recipient_phone_number",
    "message": "This is an anonymous SMS!",
    "key": "textbelt"
}

response = requests.post(url, data=data)
print(response.json())