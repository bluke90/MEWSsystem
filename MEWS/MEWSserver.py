
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import speech_recognition as sr
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
        #######################################################
        bodySplit = body.split(" ")
        range15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        #############
        stormWarn1 = bodySplit.count('tornado')
        stormWarn1x = bodySplit.count('tornados')
        stormWarn2 = body.count('solar flare')
        stormWarn3 = bodySplit.count('storm')
        stormWarn4 = bodySplit.count('earthquake')
        stormWords = (stormWarn1 + stormWarn2 +stormWarn3 + stormWarn4)
        print(stormWords)
        ###################################
        atkWrn = bodySplit.count('attacked')
        atkWrn1 = bodySplit.count('attack')
        atkWrn2 = bodySplit.count('invasion')
        atkWrn3 = bodySplit.count('nuke')
        atkWrn4 = bodySplit.count('nuclear')
        atkWords = (atkWrn + atkWrn1 + atkWrn2 + atkWrn3 + atkWrn4)
        #######################################################
        if stormWords in range15 or atkWords in range15:
            response_message = 'Intel From: {}, Intel Reads:{}'.format(number, __bodyResp)
            message = client.messages \
                .create(
                    body = response_message,
                    from_ = '+16013745980',
                    to = '+16012873833'
                )
            print("Intel Sent to Administrator")


@app.route("/record", methods=['GET', 'POST'])
def record():
    account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
    auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
    client
    # Start our TwiML response
    response = VoiceResponse()
    # Use <Say> to give the caller some instructions
    response.say('Thanks   you   for   calling   the   Mississippi   Early   Warning   System. Thank  you  for  any  intel  provided.')
    # Use <Record> to record the caller's message
    response.record(transcribe="true")
#    with open("recording.txt", "x") as f:
#       f.write(vResp)
    # End the call with <Hangup>
    response.hangup()
    return str(response)

if __name__ == '__main__':
    app.run()



