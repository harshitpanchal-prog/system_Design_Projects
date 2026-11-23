from flask import Flask

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return "Hello from Server 2!\n", 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
