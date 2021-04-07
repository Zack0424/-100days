import turtle as t
import random



isRaceOn = False
screen = t.Screen()
screen.setup(width=500,height=400)
winner = screen.textinput(title= "Make your bet: ", prompt="Which turtle will win the race?")
colors = ["red","orange","yellow", "green", "blue", "purple"]
turtles = []
if winner:
    isRaceOn = True
"""
tim.pensize(4)

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.back(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
def clear():
    # tim.setpos(0.00,0.00)
    # tim.clear()
    tim.reset()
screen.listen()
screen.onkeypress(key= "w" , fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key= "c", fun= clear)
"""
for i in range(1,7):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, i * 40 - 140)
    new_turtle.color(colors[-i])
    turtles.append(new_turtle)
while isRaceOn:
    for i in turtles:
        i.forward(random.randint(0,10))
        if i.xcor()> 230:
            isRaceOn = False

            if winner == i.pencolor():
                print(f"You won! The winner was:{i.pencolor()}")
            else:
                print(f"You lost! The winner was:{i.pencolor()}")
            screen.bye()

screen.mainloop()