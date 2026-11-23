import requests

LB_URL = "http://127.0.0.1:5000/"

for i in range(1, 7):
    resp = requests.get(LB_URL)
    print(f"Request {i}: {resp.text.strip()}")
