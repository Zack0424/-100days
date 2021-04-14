import requests
import datetime as dt

USERNAME = "zack"
TOKEN = "jkasdfhyxcvklmnasdf"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
question = input("How much time did you program today?")

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# response.raise_for_status()

today = dt.datetime.now().strftime("%Y%m%d")

pixel_post_config = {
    "date":today,
    "quantity": question,

}

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_post_endpoint,json=pixel_post_config, headers=headers)
print(response.text)
# pixel_put_config = {
#     "quantity":question
# }

# # response = requests.put(f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}",json=pixel_put_config,headers= headers)
# delete_endpoint = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=headers)