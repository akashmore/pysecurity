from __future__ import print_function
from io import BytesIO
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
import pymysql
import os
import Tkinter as tk
from Tkinter import *
from time import *
import pythoncom,pyHook,sys
import time
a=tk.Tk()
#---------------------------------------------------Db connection----------------------------------------------------------------------------------------------------------#
conn = pymysql.connect(host='localhost', port=3306, user="root",passwd='',db="login")
cur = conn.cursor()
#------------------------------------------------registration---------------------------------------------------------------------------------------------------------------------#    
def register():
    os.system("register.py")
#------------------------------------------------registration---------------------------------------------------------------------------------------------------------------------#    
def reRegister():
    os.system("reRegister.py")
#---------------------------------------------------------keyboard----------------------------------------------------------------------------------------------------#
pwdCharacters=list()
timings=list()
timeTaken=0;
def click(key):
    millis=float(round(time.time()))
    currentCharacter=list()
    pwdCharacters.append(key.char)
    currentCharacter.append(key.char)

    str=''.join(currentCharacter)
    if(str.isspace()):
        print(timings)
        global timeTaken
        timeTaken=max(timings)-min(timings)
        '''b=tk.Tk()
        b.title("registration success")
        b.geometry("500x200+500+200")
        str1="Time taken to enter the password:%d seconds"%timeTaken          Uncomment to Print timing to enter the password
        bl1=tk.Label(b,text=str1)
        bl1.place(x="50",y="60")'''
    timings.append(millis)
#------------------------------------------------unsuccessful login---------------------------------------------------------------------------------------------------------------------#     
def unsuccessful():
    global timeTaken;
    timeTaken=0;
    c=tk.Tk()
    c.title("login failed")
    c.geometry("200x200+200+200")
    cl1=tk.Label(c,text="login failed")
    cl1.place(x="50",y="60")
#----------------------------------------------------login----------------------------------------------------------------------------------------------------------#  
def login():
     #print(text1.get())
     global timeTaken;
     b=uname.get()
     c=pwd.get()
     text1.delete(0,END)
     text2.delete(0,END)
     query="SELECT * FROM `test` WHERE uname='{}' and password='{}'".format(b,c)
     if(cur.execute(query)):
           cnt=cur.fetchone()
           print(cnt)
           print(timeTaken)
           if(cnt[2]==timeTaken):
             b=tk.Tk()
             b.title("login success")
             b.geometry("200x200+200+200")
             bl1=tk.Label(b,text='login success')
             bl1.place(x="50",y="60")
           else:
            unsuccessful();
     else:
            unsuccessful();   
     return()
#----------------------------------------------------------------other------------------------------------------------------------------------------------------------#

def p():
     print(runame.get())
     print(rpwd.get())
def info():
     print("still not completed")
def author():
     print("eager to meet")
    

#---------------------------------------------------------------Main Method-------------------------------------------------------------------------------------------#   
a.title("login")
uname=tk.StringVar()
pwd=tk.StringVar()
b=uname.get()
c=pwd.get()
a.geometry("500x500+100+100")
l1=tk.Label(text="User name:")
l1.place(x="10",y="100")
l2=tk.Label(text="Password:")
l2.place(x="10",y="200")
#for captcha

image = ImageCaptcha(fonts=['A.ttf', 'B.ttf'])
data = image.generate('1234')
assert isinstance(data, BytesIO)
image.write('1234', 'out.png')


#end captcha



b1=tk.Button(text="Submit",command=login).place(x="200",y="300")
b2=tk.Button(text="register",command=register).place(x="300",y="300")
text1=tk.Entry(textvariable=uname)
text1.place(x="100",y="100")
text2=tk.Entry(textvariable=pwd,show="*")
text2.place(x="100",y="200")
text2.bind("<Key>",click)
mymenu = tk.Menu()
list1=tk.Menu()
list1.add_command(label='About the authors',command=author)
list1.add_command(label='Change the password',command=reRegister)
mymenu.add_cascade(label="Menu",menu=list1)
a.config(menu=mymenu)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
a.mainloop()
cur.close()
conn.close()
#---------------------------------------------------------End----------------------------------------------------------------------------------------------------------#

