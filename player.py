from turtle import Turtle


STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=288


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move_up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(0, new_y)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else :
            return False
        



