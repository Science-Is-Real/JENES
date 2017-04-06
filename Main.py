#Import Modules
from tkinter import *
import time
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
Can = Canvas(Master, width=1350, height=400)
#Biome
SkyImg = PhotoImage(file="Sky.gif")
Can.create_image(0,0,anchor=NW,image=SkyImg)
CloudsImg = PhotoImage(file="clouds.gif")
Clouds = Can.create_image(0,0,anchor=NW,image=CloudsImg)
TreesImg = PhotoImage(file="Savannah Trees.gif")
Trees = Can.create_image(0,0,anchor=NW,image=TreesImg)



blobimg = PhotoImage(file="blobbb.gif")
blob = Can.create_image(650,320,anchor=NW,image=blobimg)
geneticimg = PhotoImage(file = "Genetic Shuffle anim.gif")
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
    Can.move(Clouds, -5, 0)
    Can.move(Trees, -10, 0)
def moveLeft(event):
    Can.move(Clouds, 5, 0)
    Can.move(Trees, 10, 0)
def mate(event):
    Geneshuffle=Can.create_image(460,0,image=genticimg)
    time.sleep(1)
    Can.delete(Geneshuffle)
#Key Bindings
Master.bind("<Right>",moveRight)
Master.bind("<Left>",moveLeft)
Master.bind("<3>",mate)
##########
#Main Menu
##########
MenuG = Button(Master, text="Game", command = GameOn)
MenuB = Button(Master, text="Biology", command = BioOn)
MenuG.pack()
MenuB.pack()
