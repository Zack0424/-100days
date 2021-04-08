from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx = 50, pady = 50)

# Label
my_label = Label(text="This is a label", font=("Arial",24,"bold"))
# my_label.pack()
#my_label["text"] = "New Text"
# my_label.place(x=100,y=100)
my_label.grid(column=0,row=0)

## Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command= button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row= 0)

input = Entry()
input.grid(column=3, row=2)

window.mainloop()