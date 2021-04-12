import requests
from twilio.rest import Client
import os

MY_LAT = 48.039280
MY_LONG = 21.379930


def bring_an_umbrella(hourly):
    return [True for i in hourly if i["weather"][0]["id"] < 700]

account_sid = "ACc1f66aa2ec0db758e97af986b8b343b4"
auth_token = os.environ.get("AUTH_TOKEN")

api_key = os.environ.get("API_KEY")
OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters  ={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "exclude":"current,minutely,daily"

}




connection = requests.get(url=OMW_endpoint,params=parameters)
connection.raise_for_status()
data = connection.json()
hourly_weather = data["hourly"][:12]
if bring_an_umbrella(hourly_weather):
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Ma esni fog az eső! Ne felejtsd el az ☂☂",
        from_='+12393194914',
        to='+36306854154'
    )

    print(message.status)
