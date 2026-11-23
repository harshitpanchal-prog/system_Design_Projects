import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory dictionary: { "user_id": [timestamp1, timestamp2, ...] }
request_logs = {}

MAX_REQUESTS = 5
WINDOW_SECONDS = 60


@app.route("/data", methods=["GET"])
def get_data():
    # Identify user via X-User-ID header, query param, or fallback to client IP
    user_id = (
        request.headers.get("X-User-ID")
        or request.args.get("user_id")
        or request.remote_addr
    )

    now = time.time()
    timestamps = request_logs.get(user_id, [])

    # Keep only timestamps within the last 60 seconds
    valid_timestamps = [ts for ts in timestamps if now - ts < WINDOW_SECONDS]

    if len(valid_timestamps) >= MAX_REQUESTS:
        request_logs[user_id] = valid_timestamps
        return "Too Many Requests: Try again later.", 429

    valid_timestamps.append(now)
    request_logs[user_id] = valid_timestamps

    return jsonify({
        "user_id": user_id,
        "message": "Request successful",
        "requests_remaining": MAX_REQUESTS - len(valid_timestamps)
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
