from tkinter import *

import random

def start_game():
    R = random.randrange(int(spinMin.get()), int(spinMax.get()) + 1)

    if R == int(spinYour.get()):
        lblRes.configure(text="You won! Number was {}".format(R))
    else:
        lblRes.configure(text="You Lose! Number was {}".format(R))


window = Tk()
window.title("Number Guessing")
window.geometry('200x250')
window.resizable(False, False)

lblMin = Label(window, text="Enter minimum range: ")
lblMax = Label(window, text="Enter maximum range: ")
lblYour = Label(window, text="Enter your number: ")
lblRes = Label(window, text="")

spinMin = Spinbox(window, from_=0, to=100, width=5)
spinMax = Spinbox(window, from_=0, to=100, width=5)
spinYour = Spinbox(window, from_=0, to=100, width=5)

btn = Button(window, text="Confirm!", command=start_game)

lblMin.grid(column=0, row=0)
spinMin.grid(column=1, row=0)

lblMax.grid(column=0, row=1)
spinMax.grid(column=1, row=1)

lblYour.grid(column=0, row=2)
spinYour.grid(column=1, row=2)

btn.grid(column=0, row=4)

lblRes.grid(column=0, row=5)

window.mainloop()