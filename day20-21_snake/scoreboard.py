from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 22, "normal")
GAME_OVER_FONT = ("Arial", 40, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as f:

            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"High Score: {self.high_score}   Score: {self.score}", align=ALIGN, font=FONT)

    def eaten(self):
        self.score += 1
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGN, font=GAME_OVER_FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
