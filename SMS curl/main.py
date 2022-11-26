import requests
from requests.structures import CaseInsensitiveDict

url = "https://sms.api.sinch.com/xms/v1/1586c7369a0f4268bc4b051a621fe023/batches"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer api_key"
headers["Content-Type"] = "application/json"

data = """

  {
    "from": "447520650950",
    "to": [ "phone_number" ],
    "body": "Python runs the world!"
  }
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

