from turtle import Turtle,Screen
screen=Screen()

class Paddle(Turtle):    
    def __init__(self,position):
        super.__init__
        paddle=Turtle()
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5,stretch_len=1)
        paddle.color("white")
        paddle.penup()
        # screen.tracer(0)
        paddle.goto(350,0)  
    def go_up(self):
     new_y=self.ycor() + 20
     self.goto(self.xcor(),new_y)
    def go_down(self):
     new_y=self.ycor() - 20
     self.goto(self.xcor(),new_y)   