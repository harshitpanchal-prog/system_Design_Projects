import string
import random
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# In-memory dictionary to store short_id -> original_url
url_db = {}
BASE62_CHARS = string.digits + string.ascii_letters


def generate_short_id(length=6):
    while True:
        short_id = "".join(random.choice(BASE62_CHARS) for _ in range(length))
        if short_id not in url_db:
            return short_id


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json(silent=True) or {}
    long_url = data.get("url", "").strip()

    if not long_url:
        return jsonify({"error": "Missing 'url' in request body"}), 400

    if not long_url.startswith(("http://", "https://")):
        long_url = "https://" + long_url

    short_id = generate_short_id()
    url_db[short_id] = long_url

    short_url = f"{request.host_url}{short_id}"
    return jsonify({
        "short_id": short_id,
        "short_url": short_url,
        "original_url": long_url
    }), 201


@app.route("/<short_id>", methods=["GET"])
def redirect_url(short_id):
    original_url = url_db.get(short_id)
    if not original_url:
        return jsonify({"error": "Short URL not found"}), 404
    return redirect(original_url, code=302)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
