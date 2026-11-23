# Task 2: Rate Limiter Mini

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Usage
Send requests with `X-User-ID` header (limit is 5 requests per 60 seconds):
```bash
curl -H "X-User-ID: user_id_1" http://127.0.0.1:5001/data
```
Or run the included test script in another terminal:
```bash
python test_rate_limiter.py
```
