import turtle
import pandas
from writer import Writer
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
###Database
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
###Game mechanics
writer = Writer()
states = data.state.to_list()
guesses = []
guessed = 0


game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"Guess the State {guessed}/50",prompt="What's another state's name?").title()

    print(answer)
    if answer.lower() == "quit":
        screen.bye()
        missing_states = [i for i in states if i not in guesses]
        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("States_to_learn.csv")
        break
    elif answer in states and answer not in guesses:
        guesses.append(answer)
        guessed+=1
        state = data[data.state == answer]
        writer.write_states(answer,int(state.x),int(state.y))
        # state.state.item()



screen.mainloop()