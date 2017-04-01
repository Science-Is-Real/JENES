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
img = PhotoImage(file="backround1.ppm")
Background=Can.create_image(0,161, anchor=NW, image=img)
#Grass = Can.create_rectangle(-400,400,1725,385,fill="green")
#Biome = [Grass,Cloud]
Blob = Can.create_oval(650,385,675,360,fill="black")
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
