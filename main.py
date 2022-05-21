from turtle import Screen
from paddle import Paddle
from round  import Ball
import time
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
round = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game=True
while game:
    time.sleep(round.move_speed)
    screen.update()
    round.move()
    #Detect collision with wall
    if round.ycor()>270 or round.ycor()<-270:
        round.bounce_y()
    #Detect collision with r_paddle
    if round.distance(r_paddle)<50 and round.xcor()>320 or round.distance(l_paddle)<50 and round.xcor()<-320:
        round.bounce_x()

    #Detect R paddle Misses
    if round.xcor()>380:
        round.reset_position()

    #l_paddle
    if round.xcor()<-380:
        round.reset_position()


screen.exitonclick()
