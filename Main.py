#modules
from tkinter import *
#Variables
GameEnd = 0
master = Tk()
Bx = 0
Bxa = Bx + 50
Bxb = Bx + 75
#tkinter Stuff
Can = Canvas(master, width=1325, height=400)
#Game Loop
Can.create_rectangle(2,400,1325,385,fill="green")
Can.create_oval(Bxa,385,Bxb,360,fill="black")
Can.pack()
while True:
    #Functions
    def moveleft(event):
        print("Left")
        global Bx
        Bx = Bx - 100
    def moveright(event):
        print("Right")
        global Bx
        Bx = Bx + 100
    master.bind_all('<Left>',moveleft)
    master.bind_all('<Right>',moveright)
    master.mainloop()

