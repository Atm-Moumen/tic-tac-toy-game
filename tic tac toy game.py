from tkinter import *
from tkinter import ttk
from tkinter import messagebox
actplayer=1
p1=[]
p2=[]

root=Tk()

root.title('tic tac toy :player 1')
style=ttk.Style()
style.theme_use('classic')

b1=ttk.Button(root,text=' ')
b1.grid(row=0,column=0,sticky='nsew',ipadx=45,ipady=45)
b1.config(command= lambda :buclick(1) )

b2=ttk.Button(root,text=' ')
b2.grid(row=0,column=1,sticky='nsew',ipadx=45,ipady=45)
b2.config(command= lambda :buclick(2) )

b3=ttk.Button(root,text=' ')
b3.grid(row=0,column=2,sticky='nsew',ipadx=45,ipady=45)
b3.config(command= lambda :buclick(3) )

b4=ttk.Button(root,text=' ')
b4.grid(row=1,column=0,sticky='nsew',ipadx=45,ipady=45)
b4.config(command= lambda :buclick(4) )

b5=ttk.Button(root,text=' ')
b5.grid(row=1,column=1,sticky='nsew',ipadx=45,ipady=45)
b5.config(command= lambda :buclick(5) )

b6=ttk.Button(root,text=' ')
b6.grid(row=1,column=2,sticky='nsew',ipadx=45,ipady=45)
b6.config(command= lambda :buclick(6) )

b7=ttk.Button(root,text=' ')
b7.grid(row=2,column=0,sticky='nsew',ipadx=45,ipady=45)
b7.config(command= lambda :buclick(7) )

b8=ttk.Button(root,text=' ')
b8.grid(row=2,column=1,sticky='nsew',ipadx=45,ipady=45)
b8.config(command= lambda :buclick(8) )

b9=ttk.Button(root,text=' ')
b9.grid(row=2,column=2,sticky='nsew',ipadx=45,ipady=45)
b9.config(command= lambda :buclick(9) )




def buclick(id):
    global actplayer
    global p1
    global p2
    if(actplayer==1):
        setlayout(id,'X')
        actplayer=2
        root.title('tic tac toy :player 2')
        p1.append(id)


    else:
        setlayout(id,'O')
        actplayer = 1
        root.title('tic tac toy :player 1')
        p2.append(id)
    checkwiner()

def setlayout(id,txt):
    if(id==1):
        b1.config(text=txt)
        b1.state(['disabled'])
    if (id == 2):
        b2.config(text=txt)
        b2.state(['disabled'])
    if (id == 3):
        b3.config(text=txt)
        b3.state(['disabled'])
    if (id == 4):
        b4.config(text=txt)
        b4.state(['disabled'])
    if (id == 5):
        b5.config(text=txt)
        b5.state(['disabled'])
    if (id == 6):
        b6.config(text=txt)
        b6.state(['disabled'])
    if (id == 7):
        b7.config(text=txt)
        b7.state(['disabled'])
    if (id == 8):
        b8.config(text=txt)
        b8.state(['disabled'])
    if (id == 9):
        b9.config(text=txt)
        b9.state(['disabled'])
def checkwiner():
    winer=-1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winer=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winer = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winer = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winer = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winer = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winer = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winer = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winer = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winer = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winer = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winer = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winer = 2
    if ((7 in p1) and (5 in p1) and (3 in p1)):
        winer = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winer = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winer = 1
    if ((7 in p2) and (5 in p2) and (3 in p2)):
        winer = 2

    if(winer==1):
         messagebox.showinfo(title='Gameover',message="player 1 is the winer")
    if (winer == 2):
        messagebox.showinfo(title='Gameover', message="player 2 is the winer")





root.mainloop()