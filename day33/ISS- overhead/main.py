import requests
from datetime import datetime
import smtplib
import time








MY_LAT = 48.039280
MY_LNG = 21.379930
MY_USERNAME = "zackpublicprogramming@gmail.com"
MY_PASSWORD = "ZackProgram"

def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    return (MY_LAT-5 <iss_latitude< MY_LAT+5 and MY_LNG-5 <iss_longitude< MY_LNG+5)

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour+2
    return time_now < sunrise or time_now > sunset

while True:

    if is_night() and is_above() :
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_USERNAME, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_USERNAME,to_addrs="zackpresent@gmail.com",msg="Subject:ISS IS ABOVE\n\nThe ISS satelite can be seen if you look out the window!")
    time.sleep(60)
# BONUS: run the code every 60 seconds.



