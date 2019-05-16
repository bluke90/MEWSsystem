
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
######################
app = Flask(__name__)
input("Are you authorized?")
@app.route("/sms", methods =['POST'])
def sms():
    number = request.form['From']
    body = request.form['Body']
    array = ['invasion', 'storm']
    bodyList = list(body)
    if bodyList[0] == "X" and bodyList[1] == "2" and bodyList[2] == "7":
        account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
        auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
        client = Client(account_sid, auth_token)
        #### AUTHENTICATION REMOVAL ####
        bodyList = list(body)
        bodyResp = bodyList
        bodyResp[0] = ""
        bodyResp[1] = ""
        bodyResp[2] = ""
        __bodyResp = ''.join(bodyResp)
        ################################
        bodySplit = body.split(" ")
        stormWarn1 = bodySplit.count('tornado')
        stormWarn2 = bodySplit.count('solar flare')
        stormWarn3 = bodySplit.count('storm')
        stormWarn4 = bodySplit.count('earthquake')
        stormWords = (stormWarn1 + stormWarn2 +stormWarn3 + stormWarn4)
        range15 = [1, 2, 3, 4, 5]
        print(stormWords)
        if stormWords in range15:
            response_message = 'Intel From: {}, Intel Reads:{}'.format(number, __bodyResp)
            message = client.messages \
                .create(
                    body = response_message,
                    from_ = '+16013745980',
                    to = '+16012873833'
                )
            print("Intel Sent to Administrator")

if __name__ == '__main__':
    app.run()



