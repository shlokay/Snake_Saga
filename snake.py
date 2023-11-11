from turtle import Turtle, Screen
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move_forward()
        self.up()
        self.down()
        self.right()
        self.left()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.move_forward()

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.move_forward()

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.move_forward()

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.move_forward()
