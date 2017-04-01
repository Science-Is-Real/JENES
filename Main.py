#Import Modules
from tkinter import *
from time import sleep
#Declare Variables
Master = Tk()
#Create Canvas
Can = Canvas(Master, width=1325, height=400)
#Biome
Grass = Can.create_rectangle(-400,400,1725,385,fill="green")
Tree = Can.create_oval(40,385,50,3650,fill="green")
Cloud = Can.create_oval(70,20,110,40)
Biome = [Grass,Tree, Cloud]
#Blob
Blob = Can.create_oval(650,385,675,360,fill="black")
Can.pack()
#Functions
def moveRight(event):
    global Biome
    for x in range(0,len(Biome)):
        Can.move(Biome[x], -10, 0)
def moveLeft(event):
    global Biome
    for x in range(0,len(Biome)):
        Can.move(Biome[x], 10, 0)
#Key Bindings
Master.bind("<Right>",moveRight)
Master.bind("<Left>",moveLeft)
