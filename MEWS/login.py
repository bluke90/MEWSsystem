from tkinter import *
import time
from pymysql import cursors
import pymysql
#####
dbPass = "$aLZPhjax4BrsaV7oXiz$"
lWindow = Tk()
lWindow.geometry("220x175")
lWindow.title("MEWS Login")
###############
def lClick():
    __uID = uID.get()
    __uName = uName.get()
    __passW = passW.get()
    print("debug cp: 1")########### DEBUG CHECK 1
    auth = Label(lWindow, text="Authorizing...",font=("Areial Bold", 10))
    auth.place(x=-85,y=99)
    time.sleep(0.5)
    def authorize():
        ##############################################################
            def dbCon():
                enPassW = list(dbPass)
                enPassW[1] = ""
                enPassW[2] = ""
                enPassW[4] = ""
                enPassW[5] = ""
                enPassW[7] = ""
                enPassW[8] = ""
                enPassW[10] = ""
                enPassW[11] = ""
                enPassW[13] = ""
                enPassW[14] = ""
                enPassW[16] = ""
                enPassW[17] = ""
                unEnPassW = ''.join(enPassW)
                con = pymysql.connect(host='192.187.109.18',
                    user='root',
                    password=unEnPassW,
                    db='python1',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)
                with con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM users WHERE id = {0}".format(__uID))
                    rows = cur.fetchall()
                    for row in rows:
                        db_id = row['id']
                        db_username = row['username']
                        db_password = row['password']
                        print("debug cp: 2")###### DEBUG CHECK 2
                        print("User {0} has connected and has been authenticated".format(db_id))
                ###########
                def logon():
                    if __uName == db_username and __passW == db_password:
                        auth.configure(text='''
                        DataBase Connected
                        Credintials Have Been Authorized
                        Welcome {0}
                        '''.format(db_username))
                        print("debug logon check authorized")
                        time.sleep(.05)
                        import main
                    else:
                        authf = Label(lWindow, text="Unable to verify Credentials",font=("Areial Bold", 10))
                        authf.place(x=25,y=110)
                        time.sleep(.05)
                        print("debug logon check unauthorized")
                logon()
            dbCon()
    authorize()
            ##############################################################
###############
uIDLbl = Label(lWindow, text="User ID:")
uIDLbl.place(x=5,y=5)
#
uID = Entry(lWindow)
uID.place(x=70,y=5)
#
uNameLbl = Label(lWindow, text="Username:")
uNameLbl.place(x=5,y=27)
#
uName = Entry(lWindow)
uName.place(x=70,y=27)
#
passWLbl = Label(lWindow, text="Password:")
passWLbl.place(x=5,y=50)
#
passW = Entry(lWindow, show="*")
passW.place(x=70,y=50)
#
lBtn = Button(lWindow, text="Login", command=lClick)
lBtn.place(x=50,y=72, width=100)
#################
lWindow.mainloop()