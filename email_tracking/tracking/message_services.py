import requests
import random

msg_type_list = ["message.created", "message.replied", "message.bounced"]

api_url = "http://localhost:8000/event"
for i in range(1, 20):
    param = {"type": random.choice(msg_type_list)}  # randomly choose the type
    res = requests.post(api_url, data=param)
