import tkinter as tk
from tkinter import *
import random


win = tk.Tk()
win.configure(bg="light blue")
win.geometry("650x550")
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,10)
result.set("Guess a number between 1 to 10 ")
chances.set(3)
chances1.set(chances.get())

def fun():
  chances1.set(chances.get())
  if chances.get()>1:

    if no==choice.get():
      result.set("Congratulation YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      

    elif choice.get() > 10 or choice.get()<0:
      result.set("You just lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    
    elif no > choice.get():
      result.set("HINT:Your guess was too low: Guess a number higher ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set("HINT:Your guess was too High: Guess a number Lower ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set("Game Over You Lost!!!")


def restart():
  no=random.randint(1,10)
  result.set("Guess a number between 1 to 10 ")
  chances.set(3)
  chances1.set(chances.get())


ent1 = Entry(win, textvariable=choice, width=2,
             font=('Arial', 30), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50,
             font=('Arial', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='GUESS A NUMBER GAME',font=("Times New Roman", 20))
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaninig Chances',
             font=("Arial", 15), relief=GROOVE)
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(win, width=5, text='Play', font=('Courier', 25), command=fun, relief=RAISED)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = tk.Button(win, text='stop', width=30, command=win.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)
reset = tk.Button(win, text='Restart', width=30, command=restart,
                 bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)
win.mainloop()
