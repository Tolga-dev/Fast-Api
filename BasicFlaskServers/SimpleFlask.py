﻿
from flask import Flask

app = Flask("SecondApp")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye!"

app.run()

