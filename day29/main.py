from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers+password_symbols+password_letters

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)== 0  or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data:
                print(f"{website} | {email} | {password}", file=data)
            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(height= 200, width= 200)
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1, row= 0)


# # TEXTS
website_text  = Label(text="Website:")
website_text.grid(column=0, row= 1)

email_text = Label(text="Email/Username:")
email_text.grid(column= 0, row= 2)

password_text = Label(text= "Password:")
password_text.grid(column = 0, row= 3)

# # Entries

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry(width= 35)
email_entry.grid(column= 1, row= 2, columnspan= 2, sticky="EW" )
email_entry.insert(0,"zackpresent@gmail.com")

password_entry = Entry()
password_entry.grid(column= 1, row= 3, sticky="EW")

# # Buttons

generate_password_button = Button(text= "Generate Password", bd= 0.5, command= password_generation)
generate_password_button.grid(column=2,row= 3)

add_button = Button(text= "Add", bd= 0.5, width=36, command= add)
add_button.grid(column= 1, row= 4, columnspan=2, sticky="EW")

screen.mainloop()