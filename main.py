from tkinter import *
from PIL import Image,ImageTk
import colorgame
import rockpaperscissors
import tictactoe

win=Tk()


win.title('Game Launcher')
win.geometry('300x300')

def colorgamefunc():
	colorgame.colorprog()
	

def rpsfunc():
	rockpaperscissors.rpsprog()

def tttfunc():
	tictactoe.tttprog()
gameimg=Image.open('controller.jpg')
gameimg.thumbnail((100,100),Image.ANTIALIAS)
gamephoto=ImageTk.PhotoImage(gameimg)
Label(win,image=gamephoto).place(x=80,y=170)
Label(win,text='Games').place(x=110,y=10)
Label(win,text=' Color Game').place(x=85,y=50)
Label(win,text=' Tic-Tac-Toe').place(x=85,y=75)
Label(win,text=' Rock Paper Scissors').place(x=85,y=100)
Label(win,text=' Quit').place(x=85,y=125)
Button(win,text='1',command=colorgamefunc,bg='blue',fg='green').place(x=75,y=50)
Button(win,text='2',command=tttfunc,fg='red').place(x=75,y=75)
Button(win,text='3',command=rpsfunc,fg='yellow').place(x=75,y=100)
Button(win,text='4',command=exit,fg='blue').place(x=75,y=125)

win.mainloop()
