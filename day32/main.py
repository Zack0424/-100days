import smtplib
import datetime as dt
import random


my_email = "Zackpublicprogramming@gmail.com"
password = "ZackProgram"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="zackpresent@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")
#

# now = dt.datetime.now()
# year = now.year
# if year == 2021:
#     print("Wear a mask")
# print(year)
#
# date_of_birth = dt.datetime(year=2002 , month=4 , day=24 )
# print(date_of_birth)


today = dt.datetime.now().weekday()

if today == 0:
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="zackpresent@gmail.com",
                            msg=f"Subject:Monday Quote\n\n{random_quote}")





