import math #import check
from tkinter import *
import random


colour=["Red","Green","Blue","Pink","Black","Yellow","Purple","Violet","Orange","Indigo"]
name=["Red","Green","Blue","Pink","Black","Yellow","Purple","Violet","Orange","Indigo"]


z=2 #score

#fuctions
def score_up():
  global z
  z=math.pow(z,2)


def score_down():
  global z
  z=math.sqrt(z)


def ran():#for random namr and colour
  ch_col=random.choice(colour)
  return ch_col


def check():
  global ques
  ans=ques.get()
  if ans.lower()==nam_colour.lower():
    score_up()
    l1.configure(text=("score:",z))
  else:
    score_down()
    l1.configure(text=("score:",z))


def change():
  global col_name
  global nam_colour
  for i in range(1):
    col_name=ran()
    nam_colour=ran()
  l.configure(text=col_name,fg=nam_colour)
  ques.delete(0,"end")
  
#setting tk  
main=Tk()
main['bg']='white'
main.title("Stroop Game")
main.geometry('600x600')


#main logic begins


col_name=ran()
nam_colour=ran()


l=Label(main,text=col_name,fg=nam_colour,bg="white",font=("Arial Bold", 30))
l.place(x=250,y=130)


l1=Label(main,text=("score",z),bg="white",font=("Arial Bold", 15))
l1.place(x=50,y=40)

ques=Entry(main,text="Enter the colour here",width="30")
ques.place(x=160,y=200)

Button(main,text="Check",bg="white",command=lambda: [check(),change()]).place(x=260,y=270)

main.mainloop()