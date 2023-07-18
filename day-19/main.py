from turtle import Turtle,Screen
tim= Turtle()
screen=Screen()
def move_forward():
    tim.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()    
# functions as inputs
    #example : def fun_a():
    #             print("hello world")
    #          def fun_b():
    #          fun_a(fun_b)   
def move_backward():
    tim.backward(10)   
def turn_left():
    new_heading=tim.heading() + 10   
    tim.setheading(new_heading) 
def turn_right():
    new_heading=tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()            
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")    