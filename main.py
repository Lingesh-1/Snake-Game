import turtle as t
import food
from snake import Pambu
import time
import random as r
from score import Score

myscr=t.Screen()
myscr.title('PAMBU GAME')
myscr.setup(width=600,height=600)
myscr.bgcolor('grey')
myscr.tracer(0)



pambu=Pambu()
foods=food.Food()
sc=Score()



myscr.listen()
myscr.onkey(pambu.up,'Up')
myscr.onkey(pambu.down,'Down')
myscr.onkey(pambu.right,'Right')
myscr.onkey(pambu.left,'Left')

move=True
while move:
    myscr.update()
    time.sleep(0.1)
    pambu.moves()
    #food collsion
    if pambu.head.distance(foods)<25:
        foods.refresh()
        pambu.extend()
        sc.update()
    #wall collison
    if pambu.head.xcor()>280 or pambu.head.xcor()<-280 or pambu.head.ycor()>280 or pambu.head.ycor()<-280:
        sc.resetsc()
        # move=False
        pambu.resetpam()

    #tail collison
    for i in pambu.pambus[1:]:
        # if i==pambu.head:
        #     pass
        if pambu.head.distance(i)<10:
            # move=False
            sc.resetsc()
            pambu.resetpam()

    
   
    






































































myscr.exitonclick()