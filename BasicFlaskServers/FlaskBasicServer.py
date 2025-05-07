
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_route():
    return "Hello, World!"

@app.route("/test")
def test_page_route():
    return "This is a test page."

@app.route("/", methods=["POST"])
def post_method():
    post_data = request.form
    print(post_data)
    return "POST request received.", 200

@app.errorhandler(404)
def page_not_found(e):
    return "This page does not exist.", 404

if __name__ == "__main__":
    app.run()

