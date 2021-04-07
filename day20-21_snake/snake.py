from turtle import Turtle, Screen
screen = Screen()
MOVE_DISTANCE= 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.create_snake()

    def create_snake(self):
        self.snakes = []
        pos = 0
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos,0)
            pos -= 20
            self.snakes.append(snake)
            screen.update()
        self.head = self.snakes[0]

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())  # x és y koordinátája az előző négyzetnek
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def eat(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snakes[-1].xcor(),self.snakes[-1].ycor())
        self.snakes.append(snake)
    def reset(self):
        for i in self.snakes:
            i.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()