import pandas
import datetime as dt
import random
import smtplib


my_email = "zackpublicprogramming@gmail.com"
password = "ZackProgram"
##################### Extra Hard Starting Project ######################
letter_templates = ["letter_1.txt","letter_2.txt","letter_3.txt"]
# 1. Update the birthdays.csv
birthday_dict = pandas.read_csv("birthdays.csv").to_dict(orient="records")



# 2. Check if today matches a birthday in the birthdays.csv
for i in birthday_dict:
    birthday = dt.datetime(year=i["year"],month=i["month"],day=i["day"])
    today = dt.datetime.now()
    if today.month == birthday.month and today.day == birthday.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/{random.choice(letter_templates)}") as letter:
            letter_output = letter.read()
            letter_output = letter_output.replace("[NAME]",i["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=i["email"],msg=f"Subject:Happy Birthday!\n\n{letter_output}")


