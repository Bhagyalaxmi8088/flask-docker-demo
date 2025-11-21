from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return jsonify({"message": "Hello from Flask in Docker!"})

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app
