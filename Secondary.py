from tkinter import *
import time
import random
Master = Tk()
#Model
class Model:
    pass
class Player(Model):
    def __init__(self, food, shape, color, fins, wings):
        self.food = food
        self.shape = shape
        self.color = color
        self.fins = fins
        self.wings = wings
        self.pos = 625
class AIBlob(Model):
    def __init__(self, shape, color, fins, wings, pos):
        self.shape = shape
        self.color = color
        self.fins = fins
        self.wings = wings
        self.pos = pos
class Bush(Model):
    def __init__(self, food, pos):
        self.food = food
        self.pos = pos
Player = Player(0, "Square", "Blue", False, False)
AI1 = AIBlob("Triangle", "Green", False, False, 625)
#Controller
"""def Mate(event):
    if (625 - AI1.pos) < 7 or (AI1.pos-625)>-7:
        genepool_shape = [Player.shape, AI1.shape]
        genepool_color = [Player.color, AI1.color]
        Player.shape = genepool_shape[random.randint(0,1)]
        Player.color = genepool_color[random.randint(0,1)]
        AI1.shape = genepool_shape[random.randint(0,1)]
        AI1.color = genepool_color[random.randint(0,1)]
        print(genepool_shape+genepool_color)
        print(Player.shape+Player.color)
        AI1.pos = random.randint(1400,1500)"""
def eat():
    
    Bushno = Can.create_image(tree_pos+1350,0,anchor=NW,image=bushno)
#View
Vas = Canvas(Master, width=1325, height=800)
Can = Canvas(Master, width=1350, height=400)
def GameOn():
    Can.pack()
    Vas.pack_forget()
    MenuB.pack_forget()
    MenuG.pack_forget()
    MenuB.pack()
def BioOn():
    Vas.pack()
    Can.pack_forget()
    MenuG.pack_forget()
    MenuB.pack_forget()
    MenuG.pack()
tree_pos = 0
SkyImg = PhotoImage(file="Sky.gif")
Can.create_image(0,0,anchor=NW,image=SkyImg)
CloudsImg = PhotoImage(file="Clouds.gif")
Cloud1 = Can.create_image(1350,0,anchor=NW,image=CloudsImg)
Cloud2 = Can.create_image(-1350,0,anchor=NW,image=CloudsImg)
Cloud3 = Can.create_image(0,0,anchor=NW,image=CloudsImg)
foodBar0img = PhotoImage(file="Food Bar 0.gif")
foodBar1img = PhotoImage(file="Food Bar 1.gif")
foodBar2img = PhotoImage(file="Food Bar 2.gif")
foodBar3img = PhotoImage(file="Food Bar 3.gif")
FoodBar0 = Can.create_image(10,10,anchor=NW,image=foodBar0img)
CurBio = "Grass"
if CurBio == "Grass":
    TreesImg = PhotoImage(file="GrassLands.gif")
elif CurBio == "Savannah":
    TreesImg = PhotoImage(file="Savannah Trees.gif")
Tree1 = Can.create_image(1350,0,anchor=NW,image=TreesImg)
Tree2 = Can.create_image(-1350,0,anchor=NW,image=TreesImg)
Tree3 = Can.create_image(0,0,anchor=NW,image=TreesImg)
blobimg = PhotoImage(file="Blobbb.gif")
eatenimg = PhotoImage(file="Eaten Bush.gif")
Gblobimg = PhotoImage(file="GBlobbb.gif")
"""AIBlobbb = Can.create_image(625,325,anchor=NW,image=Gblobimg)"""
Blob = Can.create_image(625,325,anchor=NW,image=blobimg)
BioCount=0
BioClount=0
MenuG = Button(Master, text="Game", command = GameOn)
MenuB = Button(Master, text="Biology", command = BioOn)
MenuG.pack()
MenuB.pack()
def Eat(event):
    global Player
    if Player.food == 0:
        FoodBar1 = Can.create_image(10,10,anchor=NW,image=foodBar1img)
    if Player.food == 1:
        FoodBar2 = Can.create_image(10,10,anchor=NW,image=foodBar2img)
    if Player.food == 2:
        FoodBar3 = Can.create_image(10,10,anchor=NW,image=foodBar3img)
    Player.food += 1
    if Player.pos >= 4:
        Can.delete(FoodBar1)
        Can.delete(FoodBar2)
        Can.delete(FoodBar3)
def moveRight(event):
    Can.move(Tree1, -10, 0)
    Can.move(Tree2, -10, 0)
    Can.move(Tree3, -10, 0)
    Can.move(Cloud1, -5, 0)
    Can.move(Cloud2, -5, 0)
    Can.move(Cloud3, -5, 0)
    global tree_pos
    tree_pos += 10
    global BioCount
    global BioClount
    """global AI1
    for x in range(0,random.randint(1, 5)):
        randmove = random.randint(-10,10)
        AI1.pos += randmove
        Can.move(AIBlobbb, randmove,0)
480-390
        """
    BioClount += .5
    BioCount += 1
    print(str(BioCount)+", "+str(BioClount)+", "+str(tree_pos))
    if int(BioClount) == 135:
        Can.move(Cloud1, 1350,0)
        Can.move(Cloud2, 1350,0)
        Can.move(Cloud3, 1350,0)
        BioClount = 0
    if BioCount == 135:
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
    global tree_pos
    tree_pos -=10
    global BioCount
    global BioClount
    """global AI1
    for x in range(0,random.randint(1, 5)):
        randmove = random.randint(-10,10)
        AI1.pos = AI1.pos + randmove
        Can.move(AIBlobbb, randmove,0)"""
    BioClount -= .5
    BioCount -= 1
    print(str(BioCount)+", "+str(BioClount)+", "+str(tree_pos))
    if BioClount == -135:
        Can.move(Cloud1, -1350,0)
        Can.move(Cloud2, -1350,0)
        Can.move(Cloud3, -1350,0)
        BioClount = 0
    if BioCount == -135:
        Can.move(Tree1, -1350,0)
        Can.move(Tree2, -1350,0)
        Can.move(Tree3, -1350,0)
        BioCount = 0
Master.bind("<Right>",moveRight)
Master.bind("<Left>",moveLeft)
Master.bind("<f>",Eat)
