import requests

URL = "http://127.0.0.1:5001/data"
HEADERS = {"X-User-ID": "user_id_1"}

for i in range(1, 8):
    resp = requests.get(URL, headers=HEADERS)
    print(f"Request {i}: Status={resp.status_code} | Body={resp.text.strip()}")
