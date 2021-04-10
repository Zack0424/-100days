from tkinter import *
import pandas
import random
from google_speech import Speech
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
LANG = "ja"
chosen_word = {}

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg= BACKGROUND_COLOR)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except Exception:
    data = pandas.read_csv("data/FlashCards.csv")
finally:
    words= data.to_dict(orient="records")

#---------------------------------- -----------------------------------#


def remove():
    try:
        words.remove(chosen_word)
    except IndexError:
        messagebox.showinfo(title="There are no more words!",message="You learned every word!")
    to_learn = pandas.DataFrame(words)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(word_text,fill="white",text= chosen_word["English"])
    canvas.itemconfig(title_text,fill="white", text="English")


def next_card():
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    chosen_word= random.choice(words)
    canvas.itemconfig(title_text,text="Japanese", fill="black")
    canvas.itemconfig(card_background, image=card_image)
    canvas.itemconfig(word_text,text=chosen_word["Japanese"], fill="black")
    flip_timer = window.after(3000, flip)



    speech = Speech(chosen_word["Japanese"] + " ::2", LANG)
    speech.play()

#---------------------------------- -----------------------------------#
card_image = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

wrong_button_image= PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")


canvas = Canvas(height= 526, width= 800, bg = BACKGROUND_COLOR, border =0, highlightthickness=0)
card_background = canvas.create_image(400,263,image=card_image)
canvas.grid(column=0,row=0, columnspan=2)

flip_timer = window.after(3000, flip)

title_text= canvas.create_text(400,150,text="Japanese",font=("Ariel",40,"italic"))

word_text = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

right_button = Button(image=right_button_image, highlightthickness=0, command=remove)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_image, highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


#---------------------------------- -----------------------------------#
next_card()




window.mainloop()
