import requests

from datetime import  datetime

USERNAME = "xenia"
TOKEN = "secret"
endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
date = today.strftime("%Y%m%d")
graph_config = {
    "date": date,
    "quantity": "2.0"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


