#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Home route that returns a JSON payload."""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(debug=True)
