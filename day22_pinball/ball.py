from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.xwhere = 1
        self.ywhere = 1
        self.move_speed = 0.1
    def collision(self):
        self.ywhere *=-1
    def move(self):
        new_x = self.xcor() +10 *self.xwhere
        new_y = self.ycor() +10 *self.ywhere
        self.goto(new_x,new_y)
    def paddle_collision(self):
        self.xwhere *=-1
        self.move_speed *= 0.9
    def resetpos(self):
        self.goto(0,0)
        self.xwhere*=-1
        self.move_speed = 0.1