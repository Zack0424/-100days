from tkinter import *


screen = Tk()
screen.title("Mile to Km Converter")
screen.config(padx=20,pady=20)


km_input = Entry(text="0", width=7)
km_input.grid(column= 1, row=0)

def calculate_mile2km():
    x = float(km_input.get())
    x = round(x* 1.609,2)
    equals.config(text=x)


miles = Label(text="Miles")
miles.grid(column=2,row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

equals = Label(text="0")
equals.grid(column=1,row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_mile2km)
calculate.grid(column=1, row= 2)

screen.mainloop()