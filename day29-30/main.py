from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {website:{
            "email": email,
            "password":password
        }
    }

    if len(website)== 0  or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json","r") as data_file:
                # Reading the old data
                data = json.load(data_file)
                # Updating old data
                data.update(new_data)

        except json.decoder.JSONDecodeError or FileNotFoundError:
            data = new_data

        with open("data.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            searched = data[website]
    except KeyError:
        messagebox.showinfo(title=website, message="This website is not in the database")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="The Database is not yet created!")
    else:
        messagebox.showinfo(title=website, message=f"Email: {searched['email']}\nPassword: {searched['password']}\nThe password is copied!")
        pyperclip.copy(searched["password"])

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

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="EW",padx= 2, pady=2)

email_entry = Entry(width= 35)
email_entry.grid(column= 1, row= 2,columnspan= 2, sticky="EW",padx= 2, pady=2 )
email_entry.insert(0,"zackpresent@gmail.com")

password_entry = Entry()
password_entry.grid(column= 1, row= 3, sticky="EW",padx= 2, pady=2)

# # Buttons

generate_password_button = Button(text= "Generate Password", bd= 0.5, command= password_generation)
generate_password_button.grid(column=2,row= 3, pady=5)

add_button = Button(text= "Add", bd= 0.5, width=36, command= add)
add_button.grid(column= 1, row= 4, columnspan=2, sticky="EW")

search_button = Button(text="Search", bd= 0.5, command=search )
search_button.grid(column=2,row=1,sticky="EW")
screen.mainloop()