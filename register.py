from __future__ import print_function
import pymysql
import os
import Tkinter as tk
from Tkinter import *
from time import *
import pythoncom,pyHook,sys
import time
#----------------------------------------------------Db connection----------------------------------------------------------------------------------------------------------#
conn = pymysql.connect(host='localhost', port=3306, user="root",passwd='',db="login")
cur = conn.cursor()
#-------------------------------------------------------clear----------------------------------------------------------------------------------------------------------#
def clear():
    print('bar')
	
#-------------------------------------------------------Check the username----------------------------------------------------------------------------------------------------#
def checkUserName(event):
	b=unamer.get()
	query="SELECT * FROM `test` WHERE uname='{}'".format(b)
	if(cur.execute(query)):
		etext1.delete(0, END)
		etext1.focus()
		b1=tk.Tk()
		b1.title("Username notice")
		b1.geometry("500x200+500+200")
		str1="Username already exists"
		bl1=tk.Label(b1,text=str1)
		bl1.place(x="50",y="60")
#---------------------------------------------------------keyboard----------------------------------------------------------------------------------------------------#

totalTiming=0 #To store all the timings for further computation
pwdAvgTiming=0;
 
#This is for typing password for the first time
pwdCharacters1=list()
timings1=list()
def click1(key):
	millis=int(round(time.time()))
	currentCharacter=list()
	pwdCharacters1.append(key.char)
	currentCharacter.append(key.char)
	str=''.join(currentCharacter)
	if(str.isspace()):
		global totalTiming
		timeTaken=max(timings1)-min(timings1)
		totalTiming+=timeTaken
		'''print(timeTaken)
		b=tk.Tk()
		b.title("registration success")
		b.geometry("500x200+500+200")
		str1="Time taken to enter the password first time:%d seconds"%timeTaken
		bl1=tk.Label(b,text=str1)
		bl1.place(x="50",y="60")'''
	timings1.append(millis)
	
#This is for typing password for the second time
pwdCharacters2=list()
timings2=list()
def click2(key):
	millis=int(round(time.time()))
	currentCharacter=list()
	pwdCharacters2.append(key.char)
	currentCharacter.append(key.char)
	str=''.join(currentCharacter)
	if(str.isspace()):
		global totalTiming
		timeTaken=max(timings2)-min(timings2)
		totalTiming+=timeTaken
		'''print(timeTaken)
		b=tk.Tk()
		b.title("registration success")
		b.geometry("500x200+500+200")
		str1="Time taken to enter the password first time:%d seconds"%timeTaken
		bl1=tk.Label(b,text=str1)
		bl1.place(x="50",y="60")'''
	timings2.append(millis)
	
#This is for typing password for the third time
pwdCharacters3=list()
timings3=list()
def click3(key):
	millis=int(round(time.time()))
	currentCharacter=list()
	pwdCharacters3.append(key.char)
	currentCharacter.append(key.char)
	str=''.join(currentCharacter)
	if(str.isspace()):
		global totalTiming
		timeTaken=max(timings3)-min(timings3)
		totalTiming+=timeTaken
		'''print(timeTaken)
		b=tk.Tk()
		b.title("registration success")
		b.geometry("500x200+500+200")
		str1="Time taken to enter the password first time:%d seconds"%timeTaken
		bl1=tk.Label(b,text=str1)
		bl1.place(x="50",y="60")'''
	timings3.append(millis)

#----------------------------------------------------registration---------------------------------------------------------------------------------------------------------------------#    
def uregister():
	global pwdAvgTiming,totalTiming
	a=unamer.get()
	b=pwdr.get()
	c=r1pwd.get()
	d=r2pwd.get()
	pwdAvgTiming=totalTiming/3;
	if(b==c and c==d and b==d):
		'''print(a)
		print(b)
		print(c)
		print(d)
		print(totalTiming)
		print(pwdAvgTiming)'''
		query1="INSERT INTO test(uname,password,avgtime) VALUES('{}','{}','{}')".format(a,b,pwdAvgTiming)
		if(cur.execute(query1)):
			b=tk.Tk()
			b.title("registration success")
			b.geometry("200x200+200+200")
			bl1=tk.Label(b,text='registration success')
			bl1.place(x="50",y="60")
			conn.commit()
		else:
			c=tk.Tk()
			c.title("registration failed")
			c.geometry("200x200+200+200")
			cl1=tk.Label(c,text="registration failed")
			cl1.place(x="50",y="60")
			return()
			conn.commit()
	else:
		b=tk.Tk()
		b.title("Warning")
		b.geometry("500x200+500+200")
		str1="Passwords mismatch found"
		bl1=tk.Label(b,text=str1)
		bl1.place(x="50",y="60")
#------------------------------------------------------Main Method----------------------------------------------------------------------------------------------------------------#	 
e=tk.Tk()
e.title("register")
unamer=tk.StringVar()
pwdr=tk.StringVar()
r1pwd=tk.StringVar()
r2pwd=tk.StringVar()
e.geometry("500x500+100+100")
e1=tk.Label(e,text='register')
e1.pack()
e2=tk.Label(e,text="User name:")
e2.place(x="10",y="100")
e3=tk.Label(e,text="Password:")
e3.place(x="10",y="200")
e4=tk.Label(e,text="Retype Password:")
e4.place(x="10",y="300")
e5=tk.Label(e,text="Retype Password:")
e5.place(x="10",y="400")
etext1=tk.Entry(e,textvariable=unamer)
etext1.bind("<FocusOut>",checkUserName)
etext1.place(x="100",y="100")
etext2=tk.Entry(e,textvariable=pwdr,show="*")
etext2.place(x="100",y="200")
etext2.bind("<Key>",click1)
etext3=tk.Entry(e,textvariable=r1pwd,show="*")
etext3.place(x="110",y="300")
etext3.bind("<Key>",click2)
etext4=tk.Entry(e,textvariable=r2pwd,show="*")
etext4.place(x="110",y="400")
etext4.bind("<Key>",click3)
eb1=tk.Button(e,text="Submit",command=uregister)
eb1.place(x="250",y="450")
e.mainloop()