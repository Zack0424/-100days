from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(150, 1000), random.randint(-180, 280))

    def move(self):
        self.setx(self.xcor() - self.speed)

    def re(self):
        self.setpos(random.randint(300, 400), random.randint(-180, 280))

    def level_up(self):
        self.speed += 10
