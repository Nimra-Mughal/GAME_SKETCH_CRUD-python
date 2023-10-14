from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Number Guessing Game")

def GenerateNumberFunc():
    global Number
    Number = randint(0,10)

    messagebox.showinfo("A number was  Generated","Please Guess the number")

def GuessNumberFunc():
    global Number
    UserResponse = AnswerEntry.get()
    UserResponse = int(UserResponse)
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect!  Incorrect Please Guess LOwer",fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect!  Incorrect Please Guess Higher",fg="Red")
    else:
        ResultLabel.config(text="You Guess correctly Number was {}".format(Number),fg="black")
        AnswerEntry.delete(0,END)

Title = Label(root, text="Number Guessing game", font=("Arial",30))
Title.pack()

MainFrame = Frame(root)
MainFrame.pack(pady=60)

GuessNumLabel = Label(MainFrame,text="Guess a number from 0 to 10:", font=("Arial",20))
GuessNumLabel.pack()

AnswerEntry = Entry(MainFrame, font=("Arial",16))
AnswerEntry.pack(pady=10)

GenerateNumberBtn = Button(MainFrame, text="Generate Number",width=16, font=("Arial",16), background="Dodgerblue",
                           command=GenerateNumberFunc)
GenerateNumberBtn.pack()

GuessBtn = Button(MainFrame, text="Guess",width=16, font=("Arial",16), background="#15e650",command=GuessNumberFunc)
GuessBtn.pack(pady=5)

ResultLabel = Label(MainFrame,text="",font=("Arial",16))
ResultLabel.pack()

root.mainloop()



