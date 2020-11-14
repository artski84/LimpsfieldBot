import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mysql.connector

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    # Adding a test comment
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'yes' in incoming_msg:
        # someone wnats to sign up
        print('Someone is in')
        msg.body('You have been added to the Mix In')
        responded = True
    if 'no' in incoming_msg:
        print('Your reservation has been deleted')
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')        
    return str(resp)


if __name__ == '__main__':
    app.run()
