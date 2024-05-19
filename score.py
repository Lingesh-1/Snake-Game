from turtle import Turtle


ALIGN="center"
FONT=("arial",18,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc=0
        # self.highsc=0
        with open('data.txt') as data:
            self.highsc=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.scoeup()

    
    
    def scoeup(self):
        self.clear()
        self.write(f"Score={self.sc}  High Score={self.highsc}",align=ALIGN,font=FONT)
    
    def resetsc(self):
        if self.sc>self.highsc:
            self.highsc=self.sc
            with open('data.txt','w') as f:
                f.write(f'{self.highsc}')
        self.sc=0
        self.scoeup()


    # def gameovr(self):
    #     # self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over!!!",align="center",font=FONT)

    def update(self):
        self.sc+=1
        # self.clear()
        self.scoeup()