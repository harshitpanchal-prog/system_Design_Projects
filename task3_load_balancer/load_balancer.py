import itertools
import requests
from flask import Flask, request, Response

app = Flask(__name__)

BACKEND_SERVERS = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003",
]

# Round-robin iterator cycling through Server 1 -> Server 2 -> Server 3 -> Server 1
server_pool = itertools.cycle(BACKEND_SERVERS)


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    target_server = next(server_pool)
    target_url = f"{target_server}/{path}" if path else target_server

    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            params=request.args,
            data=request.get_data(),
            timeout=5,
        )
        return Response(resp.content, status=resp.status_code)
    except requests.RequestException as exc:
        return f"Backend server unavailable ({target_server}): {exc}\n", 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
