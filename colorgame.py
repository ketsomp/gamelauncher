from tkinter import *
from tkinter import ttk
import random
import tkinter

colors=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=30

def colorprog():

	window=Tk()

	def startGame(entry):
		if timeleft==30:
			countdown()
		nextColor()
	def nextColor():
		global score
		global timeleft
		if timeleft>0:
			e.focus_set()
			if e.get().lower()==colors[1].lower():
				score+=1
			e.delete(0,tkinter.END)
			random.shuffle(colors)
			lc.config(fg=str(colors[1]),text=str(colors[0]))
			l4.config(text='Score: '+str(score))
	def countdown():
		global timeleft
		if timeleft>0:
			timeleft-=1
			l3.config(text='Time: '+str(timeleft))
			l3.after(1000,countdown)
	def exitb():
		global timeleft
		timeleft=30
		window.destroy()
	window.title('Color Game')
	window.geometry("500x300")
	l1=Label(window,text='Objective: Type the color of the word and not the word itself').place(x=60,y=30)
	l2=Label(window,text='Press Enter to start').place(x=180,y=50)
	l3=Label(window,text='Time:')
	l3.place(x=210,y=70)
	l4=Label(window,text='Score: ')
	l4.place(x=200,y=90)
	lc=Label(window,font=('Helvetica',60))
	lc.pack()
	lc.place(x=200,y=150)
	e=Entry(window,width=10)
	e.focus_set()
	e.place(x=200,y=240)
	Button(window)
	qbb=Button(window,text='Quit',command=exitb)
	qbb.place(x=65,y=245)

	window.bind('<Return>',startGame)
	e.focus_set()
	window.mainloop()