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
#---------------------------------------------------Check the username----------------------------------------------------------------------------------------------------#
def checkUserName(event):
	b=unamer.get()
	query="SELECT * FROM `test` WHERE uname='{}'".format(b)
	rows=cur.execute(query)
	if(rows==0):
		etext1.delete(0, END)
		etext1.focus()
		b1=tk.Tk()
		b1.title("Username notice")
		b1.geometry("500x200+500+200")
		str1="Username does not exist"
		bl1=tk.Label(b1,text=str1)
		bl1.place(x="50",y="60")
	return;
#-------------------------------------------------------Check the password----------------------------------------------------------------------------------------------------#
def checkPwd(event):
	unm=unamer.get()
	pwd=currpwd.get()
	query="SELECT * FROM `test` WHERE uname='{}'".format(unm)
	if(cur.execute(query)):
		cnt=cur.fetchone()
		if(cnt[1]!=pwd):
			ecurrpwd.delete(0, END)
			ecurrpwd.focus()
			b1=tk.Tk()
			b1.title("Password notice")
			b1.geometry("500x200+500+200")
			str1="You have entered the wrong password"
			bl1=tk.Label(b1,text=str1)
			bl1.place(x="50",y="60")
	return;

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
#-------------------------------------------------------Check duplicate passwords----------------------------------------------------------------------------------------------------#
def duplicatePwd(event):
	global timeTaken
	timeTaken=0
	a=currpwd.get()
	b=pwdr.get()
	c=r1pwd.get()
	d=r2pwd.get()
	if(a==b):
		etext2.delete(0, END)
		etext3.delete(0, END)
		etext4.delete(0, END)
		etext2.focus()
		b1=tk.Tk()
		b1.title("Password notice")
		b1.geometry("500x200+500+200")
		str1="Sorry but you cant set the old password again"
		bl1=tk.Label(b1,text=str1)
		bl1.place(x="50",y="60")
	return;
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
		query1="UPDATE `test` set password='{}',avgtime='{}' where uname='{}'".format(b,pwdAvgTiming,a)
		if(cur.execute(query1)):
			print('registration success')
			b=tk.Tk()
			b.title("registration success")
			b.geometry("200x200+200+200")
			bl1=tk.Label(b,text='registration success')
			bl1.place(x="50",y="60")
			conn.commit()
		else:
			print('registration failed')
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
e.title("Change the password")
unamer=tk.StringVar()
currpwd=tk.StringVar()
pwdr=tk.StringVar()
r1pwd=tk.StringVar()
r2pwd=tk.StringVar()
e.geometry("600x600+100+100")
e1=tk.Label(e,text='Change your password or save the sample again')
e1.pack()
e2=tk.Label(e,text="User name:")
e2.place(x="10",y="100")
epwd=tk.Label(e,text="Current Password:")
epwd.place(x="10",y="200")
e3=tk.Label(e,text="New Password:")
e3.place(x="10",y="300")
e4=tk.Label(e,text="Retype New Password:")
e4.place(x="10",y="400")
e5=tk.Label(e,text="Retype New Password:")
e5.place(x="10",y="500")
etext1=tk.Entry(e,textvariable=unamer)
etext1.bind("<FocusOut>",checkUserName)
etext1.place(x="150",y="100")
ecurrpwd=tk.Entry(e,textvariable=currpwd,show="*")
ecurrpwd.place(x="150",y="200")
ecurrpwd.bind("<FocusOut>",checkPwd)
etext2=tk.Entry(e,textvariable=pwdr,show="*")
etext2.place(x="150",y="300")
etext2.bind("<Key>",click1)
etext3=tk.Entry(e,textvariable=r1pwd,show="*")
etext3.place(x="150",y="400")
etext3.bind("<Key>",click2)
etext4=tk.Entry(e,textvariable=r2pwd,show="*")
etext4.place(x="150",y="500")
etext4.bind("<FocusOut>",duplicatePwd)
etext4.bind("<Key>",click3)
eb1=tk.Button(e,text="Submit",command=uregister)
eb1.place(x="250",y="550")
e.mainloop()