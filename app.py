import os
from app import create_app
# from flask import Flask
# if os.path.exists("env.py"):
#     import env


# app = Flask(__name__)
app = create_app()


# @app.route("/")
# def hello():
#     return "In the words of Théoden....<br>'So... it beings...'"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  