from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = ""
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg= GREEN)
    checkmark_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps %8 == 0:
        timer_label.config(text="Break", fg=GREEN)
        countdown(long_break_sec)

    elif reps %2 == 0:
        timer_label.config(text="Break", fg =PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", fg=RED)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global check
    global checkmark_label
    minute = count // 60
    second = count % 60
    # if second < 10:
    #     second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute:02}:{second:02}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        if reps%2 == 0:
            check += "✅"
            checkmark_label.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"), fg= GREEN, bg= YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", highlightthickness= 0, borderwidth = 0, command= start_timer)
start_button.grid(column=0, row= 2)

reset_button = Button(text="Reset", highlightthickness= 0, borderwidth = 0, command= reset_timer)
reset_button.grid(column=2, row= 2)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column = 1, row = 3)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=tomato_image)

timer_text = canvas.create_text(100,130, text= "00:00", fill= "white", font=(FONT_NAME,28,"bold") )
canvas.grid(column=1, row= 1)





window.mainloop()