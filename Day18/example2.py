import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
colours=["DarkOrchid","DeepSkyBlue","IndianRed","wheat","Slategrey","SeaGreen","Red","Yellow"]
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)    
    random_color=(r, g, b)
    return random_color
    
directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))