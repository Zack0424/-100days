import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla INC"

account_sid = "ACc1f66aa2ec0db758e97af986b8b343b4"
auth_token = os.environ.get("AUTH_TOKEN")
up_or_down:str


parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"IBM",
    "apikey":os.environ.get("ALPHA_API_KEY")
}

connection = requests.get("https://www.alphavantage.co/query",params=parameters)
connection.raise_for_status()
data = connection.json()['Time Series (Daily)']

data_list = [i for i in data]
yesterday = float(data[data_list[0]]['4. close'])
before_it = float(data[data_list[1]]['4. close'])
move = int((1-(yesterday/before_it)) *1000)
if move >= 5 or move <= -5:
    newsapi = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

    top_headlines = newsapi.get_everything(q=COMPANY_NAME,language='en')
    top_headlines = top_headlines['articles'][:3]
    if move >0: up_or_down = f"{COMPANY_NAME}: 🔺{abs(move)}%"
    else: up_or_down = f"{COMPANY_NAME}: 🔻{abs(move)}%"

    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body=up_or_down,
        from_='+12393194914',
        to='+36306854154'
    )
    for i in top_headlines:
        title = i['title']
        description = i['description']
        client = Client(account_sid,auth_token)
        message = client.messages \
            .create(
            body=f"\nHeadline: {title}\nBrief: {description}",
            from_='+12393194914',
            to='+36306854154'
        )


