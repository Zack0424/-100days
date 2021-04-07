from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 22, "normal")



class Scoreboard(Turtle):
    def __init__(self, x,y):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def won(self):
        self.clear()
        self.score+=1
        self.update_text()