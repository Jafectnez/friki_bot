"""
app.py

Author: Allan Martínez
"""
from os import environ

from flask import Flask
from flask_restful import Api

from bot import init_bot

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    """Root route.

    Returns:
        Str: Simple hello world response
    """
    init_bot()
    return "Bot Listening..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))
