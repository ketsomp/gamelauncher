from tkinter import *
import tkinter.messagebox as msg
import random
from PIL import Image,ImageTk

userscore=compscore=0
uc=cc=''
rounds=0
def rpsprog():

	

	rps=Toplevel()
	rps.geometry('340x300')
	rps.title('Rock Paper Scissors')

	def choicetonumber(choice):
		rpss={'scissor':0,'paper':1,'rock':2}
		return rpss[choice]
	def numbertochoice(number):
	        rpss={'scissor':0,'paper':1,'rock':2}
	        return rpss[number]
	def rcc():
		return random.choice(['scissor','paper','rock'])
	def result(hchoice,cchoice):
		global userscore
		global compscore
		global rounds
		user=choicetonumber(hchoice)
		comp=numbertochoice(cchoice)
		if user==comp:
			statusl.configure(image=tiephoto)
			roundsl.configure(text=f'Rounds: {rounds}')
			rounds+=1
		elif ((user-comp)%3==1):
			statusl.configure(image=losephoto)
			roundsl.configure(text=f'Rounds: {rounds}')
			compscore+=1
			rounds+=1
		else:
			statusl.configure(image=winphoto)
			roundsl.configure(text=f'Rounds: {rounds}')
			userscore+=1
			rounds+=1
		userchoice.configure(text=f'Your Choice: ')
		compchoice.configure(text=f"Computer's Choice: ")
		userscorel.configure(text=f'Your Score: {userscore}')
		compscorel.configure(text=f"Computer's Score: {compscore}")
		if uc=='rock':
			userchoicepic.configure(image=rockphoto)
		elif uc=='paper':
			userchoicepic.configure(image=paperphoto)
		else:
			userchoicepic.configure(image=scissorphoto)
		if cc=='rock':
			compchoicepic.configure(image=rockphoto)
		elif cc=='paper':
			compchoicepic.configure(image=paperphoto)
		else:
			compchoicepic.configure(image=scissorphoto)

	def rock():
		global uc 
		global cc 
		uc='rock'
		cc=rcc()
		result(uc,cc)
	def paper():
		global uc 
		global cc 
		uc='paper'
		cc=rcc()
		result(uc,cc)
	def scissor():
		global uc 
		global cc 
		uc='scissor'
		cc=rcc()
		result(uc,cc)

	def resetbutton():
		global userscore, compscore, rounds
		userscore=compscore=rounds=0
		userscorel.configure(text=f"Your Score: {userscore}")
		compscorel.configure(text=f"Computer's Score: {compscore}")
		roundsl.configure(text=f'Rounds: {rounds}')
	def exitf():
		resetbutton()
		rps.destroy()

	rockimg=Image.open('rock.png')
	rockimg.thumbnail((30,50),Image.ANTIALIAS)
	rockphoto=ImageTk.PhotoImage(rockimg)
	paperimg=Image.open('paper.png')
	paperimg.thumbnail((30,30),Image.ANTIALIAS)
	paperphoto=ImageTk.PhotoImage(paperimg)
	scissorimg=Image.open('scissor.png')
	scissorimg.thumbnail((30,30),Image.ANTIALIAS)
	scissorphoto=ImageTk.PhotoImage(scissorimg)
	rpsimg=Image.open('rps.png')
	rpsimg.thumbnail((100,100),Image.ANTIALIAS)
	rpsphoto=ImageTk.PhotoImage(rpsimg)
	winimg=Image.open('youwin.png')
	winimg.thumbnail((100,100),Image.ANTIALIAS)
	winphoto=ImageTk.PhotoImage(winimg)
	loseimg=Image.open('youlose.png')
	loseimg.thumbnail((100,100),Image.ANTIALIAS)
	losephoto=ImageTk.PhotoImage(loseimg)
	tieimg=Image.open('tie.jpg')
	tieimg.thumbnail((90,90),Image.ANTIALIAS)
	tiephoto=ImageTk.PhotoImage(tieimg)

	rpsl=Label(rps,image=rpsphoto)
	rpsl.place(x=110,y=60)
	br=Button(rps,text='Rock',image=rockphoto,command=rock)
	br.place(x=60,y=150)
	bp=Button(rps,text='Paper',image=paperphoto,command=paper)
	bp.place(x=140,y=150)
	bs=Button(rps,text='Scissor',image=scissorphoto,command=scissor)
	bs.place(x=220,y=150)
	rb=Button(rps,text='Reset',command=resetbutton)
	rb.place(x=30,y=240)
	qb=Button(rps,text='Quit',command=exitf)
	qb.place(x=250,y=240)

	userchoice=Label(rps,text='Your Choice: ')
	userchoice.place(x=10,y=40)
	compchoice=Label(rps,text="Computer's Choice: ")
	compchoice.place(x=180,y=40)
	userscorel=Label(rps,text='Your Score: ')
	userscorel.place(x=10,y=185)
	compscorel=Label(rps,text="Computer's Score: ")
	compscorel.place(x=180,y=185)
	statusl=Label(rps,text='')
	statusl.place(x=113,y=205 )
	userchoicepic=Label(rps)
	userchoicepic.place(x=100,y=30)
	compchoicepic=Label(rps)
	compchoicepic.place(x=307,y=30)
	roundsl=Label(rps,text='Rounds: ')
	roundsl.place(x=10,y=210)



	rps.mainloop()
#rpsprog()