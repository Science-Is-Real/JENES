#Import Modules
from tkinter import *
from time import sleep
#Declare Variables
Master = Tk()
#############
#Biology Side
#############
#Create Canvas
Vas = Canvas(Master, width=1325, height=800)
#Functions
def BioOn():
    Vas.pack()
    Can.pack_forget()
    MenuG.pack_forget()
    MenuB.pack_forget()
    MenuG.pack()
##########
#Game Side
##########
#Create Canvas
Can = Canvas(Master, width=1325, height=400)
#Biome
#Cloud = Can.create_oval(70,20,110,40)
img = PhotoImage(file="G.E.N.E.S\Savannah.gif")
Background=Can.create_image(0,0, anchor=NW, image=img)
blobimg = PhotoImage(file="vghvahcbkja")
blob = Can.create_image(650,320,anchor=NW,image=blobimg)
#Functions
def GameOn():
    Can.pack()
    Vas.pack_forget()
    MenuB.pack_forget()
    MenuG.pack_forget()
    MenuB.pack()
def moveRight(event):
    Can.move(Background, -10, 0)
def moveLeft(event):
    Can.move(Background, 10, 0)
#Key Bindings
Master.bind("<Right>",moveRight)
Master.bind("<Left>",moveLeft)
##########
#Main Menu
##########
MenuG = Button(Master, text="Game", command = GameOn)
MenuB = Button(Master, text="Biology", command = BioOn)
MenuG.pack()
MenuB.pack()
