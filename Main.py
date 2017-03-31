#Import Modules
from tkinter import *
from time import sleep
#Declare Variables
Master = Tk()
#Create Canvas
Can = Canvas(Master, width=1325, height=400)
Blob = Can.create_oval(10,385,35,360,fill="black")
Grass = Can.create_rectangle(2,400,1325,385,fill="green")
Can.pack()
#Functions
def moveRight(event):
    Can.move(Blob, 10, 0)
#Key Bindings
master.bind("<Right>",moveRight)
#Game Loop
