import turtle as t

POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Pambu:
    def __init__(self):
        self.pambus=[]
        self.createpambu()
        self.head=self.pambus[0]
    

  
    def createpambu(self):
        for i in POSITION:
            self.addseg(i)

    def addseg(self,i):
        pambu=t.Turtle(shape='square')
        pambu.penup()
        pambu.color('orange')
        pambu.goto(i)
        self.pambus.append(pambu)

    def resetpam(self):
        for i in self.pambus:
            i.goto(1000,1000)
        self.pambus.clear()
        self.createpambu()
        self.head=self.pambus[0]

    def extend(self):
        self.addseg(self.pambus[-1].position())
    def moves(self):
        for i in range(len(self.pambus)-1,0,-1):
            x=self.pambus[i-1].xcor()
            y=self.pambus[i-1].ycor()
            self.pambus[i].goto(x,y)
        self.head.forward(DISTANCE)
    

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)