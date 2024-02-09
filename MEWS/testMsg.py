from twilio.rest import Client
from tkinter import Tk, Label, Entry, Place, Button
#############################

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)
wWindow = Tk()
wWindow.geometry('300x100')
z = 0
def yes():
    with open('numbers.txt', 'r') as n:
        __numbers = n.read()
    n.close()
    numbers = __numbers.split('\n')
    print(numbers)
    for number in numbers:
        global z
        z += 1
        message = client.messages.create(
            body = 'This is a test of the Automatic Mississippi regional early warning system built by Blake Ganzerla to warn of natural disaster, invasion, forign or domestic attacks and more. ',
            from_ = '+16013745980',
            to = number
        )
        print(str(z) + ':' + message.status)



yLabel = Label(wWindow, text='Are you sure you want to send a test message?')
yLabel.place(x=25,y=15)
yBtn = Button(wWindow, text='yes', command=yes)
yBtn.place(x=125,y=50)
wWindow.mainloop()
