
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import datetime
######################
app = Flask(__name__)
input("Are you authorized?")

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)
@app.route("/sms", methods =['POST'])
def sms():
    ########## Numbers List ############
    with open('numbers.txt', "r") as n:#
        numbers = n.read()             #
    n.close()                          #
    numbersX = numbers.split("\n")     #
    ####################################
    ######## Get Date and time #########
    now = datetime.datetime.now()
    __now = now.strftime("%Y_%m_%d_%H_%M_%S")
    ####################################
    number = request.form['From']
    body = request.form['Body']
    bodySplit = body.split(" ")
    bodyList = list(body)
    ############ Begin processing ############
    if bodyList[0] == "X" and bodyList[1] == "2" and bodyList[2] == "7":
        account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
        auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
        client = Client(account_sid, auth_token)
        #### AUTHENTICATION REMOVAL ####
        bodyResp = bodyList
        bodyResp[0] = ""
        bodyResp[1] = ""
        bodyResp[2] = ""
        __bodyResp = ''.join(bodyResp)
        #######################################################
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
            with open(timeStamped("INTEL_MSG.txt"), "w") as f:
                f.write("Body: {0}, From: {1}, SID: {2}".format(__bodyResp, number, message.sid))
            return str(message)
        else:
            NoIntel = str("No intel Recived. No message sent.")
            return str(NoIntel)
    ####################################################################################################################################################

    elif bodyList[0] == "Z" and bodyList[1] == "2" and bodyList[2] == "7" and number == '+16012873833':
        account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
        auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
        client = Client(account_sid, auth_token)
        range15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ##### AUTHENTICATION REMOVAL #####
        bodyList = list(body)
        bodyResp = bodyList
        bodyResp[0] = ""
        bodyResp[1] = ""
        bodyResp[2] = ""
        __bodyResp = ''.join(bodyResp)
        ############################################################             #
        stormAlert = bodySplit.count('tornado')  #
        stormAlert1 = bodySplit.count('storm')   #
        stormAlertP = bodySplit.count('tornados')
        stormAlert1P = bodySplit.count('storms')
        stormAlert2 = bodySplit.count('rain')
        stormAlert3 = bodySplit.count('rainfall')
        __stormAlert = (stormAlert + stormAlertP + stormAlert1 + stormAlert1P)#
        ##########################################
        atkAlert = bodySplit.count('attack')           #
        atkAlertP = bodySplit.count('attacks')         #
        atkAlert1 = bodySplit.count('invasion')        #
        atkAlert1P = bodySplit.count('invasions')      #
        atkAlert2 = bodySplit.count('nuclear')         #
        atkAlert3 = bodySplit.count('nuke')            ###########################################
        __atkWarn = (atkAlert + atkAlertP + atkAlert1 + atkAlert1P + atkAlert2 + atkAlert3)#
       ######################################################################################
        if __stormAlert in range15:
            with open(timeStamped("STRM_MSG.txt"), "w") as f:
                for __numbers in numbersX:
                    message = client.messages \
                    .create(
                        body = "The MEWS system has detected life threatning events in the area. Intel of {0} from multiple sources.".format(__bodyResp),
                        from_ = '+16013745980',
                        to = __numbers
                    )
                    print(message.status)
                    print(message.sid)
                    print('Alert Sent')
                    f.write("Body: {0}, From: {1}, SID: {2}; \n".format(__bodyResp, number, message.sid))
                f.close()
            return str(message)
        elif __atkWarn in range15:
            message = client.messages \
                .create(
                    body = "The MEWS system has recived intel of national events that could have a life threating impact Mississippi. We have recived intel of {0} from multiple sources.".format(__bodyResp),
                    from_ = '+16013745980',
                    to = '+16012873833'
                )
            print(message.status)
            print(message.sid)
            print('Alert Sent')
            with open(timeStamped("ATK_MSG.txt"), "w") as f:
                f.write("Body: {0}, From: {1}, SID: {2}\n".format(__bodyResp, number, message.sid))
            return str(message)
        else:
            NoIntel = str("No intel Recived. No message sent.")
            with open(timeStamped('NoIntel_MSG.txt'), "w") as f:
                f.write("Body: {0}, From: {1}, SID: {2}\n".format(__bodyResp, number, message.sid))
            f.close()
            return str(NoIntel)
    else:
        NoIntel = str("No intel Recived. No message sent.")
        with open(timeStamped('NoIntel_MSG.txt'), "w") as f:
            f.write("Body: {0}, From: {1}, SID: {2}\n".format(__bodyResp, number, message.sid))
        f.close()
        return str(NoIntel)

###################################### VOICE ############################################
@app.route("/record", methods=['GET', 'POST'])
def record():
    response = VoiceResponse()
    response.say('Thanks   you   for   calling   the   Mississippi   Early   Warning   System. Thank  you  for  any  intel  provided.')
    response.record(transcribe="true")
#    with open("recording.txt", "x") as f:
#       f.write(vResp)
    response.hangup()
    return str(response)


##################################
if __name__ == '__main__':       #
    app.run()                    #
##################################


