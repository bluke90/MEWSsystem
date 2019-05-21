from tkinter import Tk, Button, Label, Entry
import time
##########################################

def addNumberX():
    __adEntry = adEntry.get()
    with open('numbers.txt', 'a') as n:
        n.write('\n' + __adEntry)
    time.sleep(.05)

anWindow = Tk()
anWindow.geometry('275x150')
anWindow.title('MEWSsystem')

adLbl = Label(anWindow, text='Number: ')
adLbl.place(x=4,y=4)
adEntry = Entry(anWindow)
adEntry.place(x=4,y=24)
adBtn = Button(anWindow, text='Add Number', command=addNumberX)
adBtn.place(x=12,y=48)


anWindow.mainloop()