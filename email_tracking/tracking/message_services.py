import requests

print("adfasdfs")

api_url = "http://localhost:9000/event"
param = {"keyss": "asdfasdf"}
res = requests.post(api_url, data=param)

print(res)
