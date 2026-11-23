# Task 1: URL Shortener Lite

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Usage
1. Shorten a URL:
```bash
curl -X POST http://127.0.0.1:5000/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.example.com/some/very/long/path"}'
```

2. Redirect using the returned `short_id`:
```bash
curl -i http://127.0.0.1:5000/<short_id>
```
