import turtle

def move_right():
    player.forward(10)
def move_left():
    player.backward(10)


player = turtle.Turtle("square")
player.color("green")
player.penup()

screen = turtle.Screen()
screen.title("Dodge_Em")
screen.screensize(500,400,"lightgray")
collision = False
player.setpos(0,-200)

while collision == False:
    screen.onkeypress(key="d", fun=move_right)
    screen.onkeypress(key="a", fun=move_left)





screen.listen()
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="a",fun=move_left)

screen.mainloop()