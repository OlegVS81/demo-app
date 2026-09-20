import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "unknown")


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b


@app.route("/")
def index():
    # os.uname() есть только на Unix; на Windows будет ошибка
    try:
        hostname = os.uname().nodename
    except AttributeError:
        # Фоллбэк для Windows
        hostname = os.environ.get("COMPUTERNAME", "unknown-host")
    return f"demo-app версии {APP_VERSION}, узел {hostname}\n"


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": APP_VERSION}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
