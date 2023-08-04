from flask import Flask, request, Response
from twilio.rest import Client
from task import open_ai

app = Flask(__name__)

account_sid = 'AC0aceaf628f633a90835a1cd97302865a'
auth_token = '7d147d2936113877cdedc0d03365fa8f'
client = Client(account_sid, auth_token)

@app.route('/', methods=['POST'])
def bot():
    msg = request.form.get("Body")
    sender_number = request.form.get("From")
    sender_name = request.form.get("ProfileName")
    # print(msg)
    if msg == "Hi":
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"hello, {sender_name}",
            to = sender_number
        )
    else:
        ans = open_ai(msg)
        client.messages.create(
            from_='whatsapp:+14155238886',
            body= ans,
            to = sender_number
        )

    return Response("Hello", status=200)

if __name__ == '__main__':
    app.run(port=5000)
