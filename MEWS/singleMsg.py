from twilio.rest import Client
from tkinter import *
#####################333
account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
client = Client(account_sid, auth_token)
smWindow = Tk()
smWindow.title("MEWS Single Recipent SMS")
def click():
    msg_body = msgEntry.get()
    number = numEntry.get()
    def send():
        message = client.messages \
            .create(
                body = msg_body,
                from_ = '+16013745980',
                to = number
            )
    send()
    
numLbl = Label(smWindow, text='Number:')
numLbl.place(x=5,y=5)
numEntry = Entry(smWindow)
numEntry.place(x=5,y=25)
#
msgLbl = Label(smWindow, text='Message:')
msgLbl.place(x=5,y=50)
msgEntry = Entry(smWindow)
msgEntry.place(x=5,y=75)
#
sendBtn = Button(smWindow, text='SEND', command=click)
sendBtn.place(x=15,y=100)

print(message.sid)
print(message.status)
