from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
segments=[]
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.new_segment=Turtle("square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.segment.append(self.new_segment)
    def move(self):
        for seg_num in range(len(segments)-1,0,-1):
            new_x=segments[seg_num-1].xcor()
            new_y=segments[seg_num-1].ycor()
            segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)



