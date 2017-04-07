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
CloudsImg = PhotoImage(file="Clouds.gif")
Cloud1 = Can.create_image(1350,0,anchor=NW,image=CloudsImg)
Cloud2 = Can.create_image(-1350,0,anchor=NW,image=CloudsImg)
Cloud3 = Can.create_image(0,0,anchor=NW,image=CloudsImg)
CurBio = "Grass"
if CurBio == "Grass":
    TreesImg = PhotoImage(file="GrassLands.gif")
elif CurBio == "Savannah":
    TreesImg = PhotoImage(file="Savannah Trees.gif")
Tree1 = Can.create_image(1350,0,anchor=NW,image=TreesImg)
Tree2 = Can.create_image(-1350,0,anchor=NW,image=TreesImg)
Tree3 = Can.create_image(0,0,anchor=NW,image=TreesImg)
blobimg = PhotoImage(file="Blobbb.gif")
Blob = Can.create_image(625,325,anchor=NW,image=blobimg)
BioCount=0
#Functions
def GameOn():
    Can.pack()
    Vas.pack_forget()
    MenuB.pack_forget()
    MenuG.pack_forget()
    MenuB.pack()
def moveRight(event):
    Can.move(Tree1, -10, 0)
    Can.move(Tree2, -10, 0)
    Can.move(Tree3, -10, 0)
    Can.move(Cloud1, -5, 0)
    Can.move(Cloud2, -5, 0)
    Can.move(Cloud3, -5, 0)
    global BioCount
    BioCount += 1
    print(BioCount)
    if BioCount == 135:
        Can.move(Cloud1, 1350,0)
        Can.move(Cloud2, 1350,0)
        Can.move(Cloud3, 1350,0)
        Can.move(Tree1, 1350,0)
        Can.move(Tree2, 1350,0)
        Can.move(Tree3, 1350,0)
        BioCount = 0
def moveLeft(event):
    Can.move(Cloud1, 5, 0)
    Can.move(Cloud2, 5, 0)
    Can.move(Cloud3, 5, 0)
    Can.move(Tree1, 10, 0)
    Can.move(Tree2, 10, 0)
    Can.move(Tree3, 10, 0)
    global BioCount
    BioCount -= 1
    print(BioCount)
    if BioCount == -135:
        Can.move(Cloud1, -1350,0)
        Can.move(Cloud2, -1350,0)
        Can.move(Cloud3, -1350,0)
        Can.move(Tree1, -1350,0)
        Can.move(Tree2, -1350,0)
        Can.move(Tree3, -1350,0)
        BioCount = 0
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
