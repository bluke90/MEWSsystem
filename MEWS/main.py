import subprocess
import os
from tkinter import *
######### FUNCTIONS ###########

def nClick(): #NEWS CLICK
    import singleMsg
    ####
def nsClick(): #NAME SEARCH CLICK
    import testMsg
    ####
def enAlg():
    import encryptionAlg
############# START ###############
window = Tk()                     #
window.geometry("400x400")        #
window.title("Proton Access Hub") #
###################################
##################
############
fTitle = Label(window, text="Welcome To Proton Services Secure Data Access Point", font=('Areial Bold',10))
fTitle.place(x=25,y=2)
#
nBtn = Button(window, text="Single Recipient SMS", command=nClick, width="50")
nBtn.place(x=17,y=25)
#
nsBtn = Button(window, text="Send Test", command=nsClick, width="50")
nsBtn.place(x=17,y=55)
#
enAlgBtn = Button(window, text="Add Number", command=enAlg, width="50")
enAlgBtn.place(x=17,y=85)
#
#
###### END ######
window.mainloop()