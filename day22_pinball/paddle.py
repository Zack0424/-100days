from turtle import Turtle

PADDLE_LEN = 4

class Paddle(Turtle):

    def __init__(self, player_position):
        super().__init__()
        self.createpaddle(player_position)
    def createpaddle(self, player_position):
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setpos(player_position)
    def up(self):
        self.sety(self.ycor()+20)
    def down(self):
        self.sety(self.ycor() - 20)