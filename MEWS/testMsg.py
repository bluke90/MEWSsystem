from twilio.rest import Client
from tkinter import *

#############################

account_sid = 'AC020f2f6306dc7ef75bc61e09cfb63a96'
auth_token = '6cfcd6fa0f0ddab26250ed24680066b9'
client = Client(account_sid, auth_token)

numbers_to_message = ['+16017505916', '+16016221389', '+16019469169', '+16012873833', '+16158011787']
for number in numbers_to_message:
    client.messages.create(
        body = 'This is a test of the Automatic Mississippi regional early warning system built by Blake Ganzerla to warn of natural disaster, invasion, forign or domestic attacks and more. ',
        from_ = '+16013745980',
        to = number
    )

print(message.status)

