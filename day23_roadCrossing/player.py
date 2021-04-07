from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.finish = FINISH_LINE_Y
        self.goto(0, -250)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def re(self):
        self.sety(-250)
