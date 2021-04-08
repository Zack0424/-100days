from turtle import Turtle
FONT = ("Arial", 8, "normal")
class Writer(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_states(self,state,x,y):
        self.goto(x,y)
        self.write(state,align="center", font=FONT)