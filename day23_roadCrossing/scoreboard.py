from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.at_level = 1
        self.penup()
        self.hideturtle()
        self.setpos(-260, 260)
        self.level()

    def level(self):
        self.clear()
        self.write(f"Level: {self.at_level}",font=FONT)

    def level_up(self):
        self.at_level += 1
        self.level()
    def game_over(self):
        gameOverMessage = Turtle()
        gameOverMessage.hideturtle()
        gameOverMessage.penup()
        gameOverMessage.write("GAME OVER",font=FONT)
