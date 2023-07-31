from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)  
screen.title("pong")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()
top_paddle=Paddle((100,100))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        # need to bounce
        ball.bounce_y()
        # detect collision with right r_paddle
        if ball.distance(r_paddle) < 50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
            ball.bounce_x()
        #Deetect when right paddle missed
        if ball.xcor()>380:
            ball.reset_position() 
            scoreboard.l_point()
        #Detect L paddle misses
        if ball.xcor<-380:
            ball.reset_position()
screen.exitonclick()   