# Web Development

## Frameworks
* applications
* web services
* resources
* api 
* automations
## Authorization
* Flask
## Templating
* 
## Rest
* Representational state transfer
  * rest
* stateless communication model and http methods for interactions
* learn how to create simple rest api - use python frameworks - flask
## ORMS
* Object relational mapping
  * oop and relational databases

# Intro
* Python + Html(hypertext makeup language) + css(cascading style sheets) and js
* Django
  * follows
    * model view controller architectural
  * fast
    * from concept to completion 
  * versatile
    * content management to social networks 
  * fully loaded
    * to handle common web development tasks
  * exceedingly scalable
    * busiest sites on web
  * reassuringly secure
* Flask
  * micro web framework
  * flexible and customizable more than django
  * for smaller projects
  * simple
    * web routes 
    * handling requests
  * jinja template
    * support for html
  * third part extensions support
  * built in server and fast debugger
* FaskAPI
  * modern
  * fasdt
  * 3.8+ based
  * microsoft and uber
  * rest api and recommended
  * openapi fro api creationg
    * path operations, paremeters, body requests, security
  * automatic data model 

# Projects
* Dropbox
  * serverside, client, api
* Netflix
* Spotify
* Instagram
* Google
* Facebook

# Common Web Apps
* HTML
* CSS
* JS
* BACKEND
* DATABASE

# Web Development and Frameworks
* web servers are based on http protocols
  * stateless
  * request response protocol in the client server computing model
  * socket programming
  * request handling
  * manager url routing


## Simple Web Applications
* Understand http
  * web servers are based on the http protocols
  * stateless
  * request response
  * client server 
  * get post, status codes, headers, and message format
* Handle Socket 
  * socket programming
  * open, close, manage connections
* Request Handler
  * build a request handler that can parse http requests and route them to functions and return responses
* Manage URL
  * Server must parse urls from requests and map them to resources 
  


```python

import http.server
import socketserver
from urllib.request import localhost


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path == "/":
            self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>This is a origin path.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == "/test":
            self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.wfile.write(bytes("This page does not exist.", "utf-8"))

PORT = 8000
handler = HttpRequestHandler

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
 

# curl localhost:8000

```

```python

import http.server
import socketserver
import urllib.parse

class HttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            self.wfile.write(bytes("Hello, World!", "utf8"))
        elif self.path == "/test":
            self.wfile.write(bytes("This is a test page.", "utf8"))
        else:
           self.wfile.write(bytes("This page does not exist.", "utf8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode("utf-8"))
        print(post_data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("POST request received.", "utf8"))

PORT = 5000
handler = HttpRequestHandler

if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", PORT), handler) as httpd:
        print("Serving at port:", PORT)
        httpd.serve_forever()

```

WFs excel in efficiency.


```python

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
```
curl.exe -X POST -d "param1=value1&param2=value2" http://127.0.0.1:5000
 

## Flask Framework introduction
* flask
  * lightweight web application framework
  * micro framework 
  * simple
  * minimalist
  * provides essential components
  * extensible
  * allowing developers to add features as needed
* flask keys
  * flexible
  * jinja2 templating
    * presentation layer from business logic separation
  * built in development server
  * extensions
    * authentication
    * database integrations
    * restful api
  * werkzeug
    * toolkit, solid foundation for handling http request and responses

## A typical web application using a web framework
* flask security
  * authentication
  * role
  * permission management
  * password hashing
* pydantic or mashmallow 
  * can validate user data
* Sql alchemy
  * python orm
    * object relational mapping lib
* django
  * authentication 
  * authorization

## Flask Routing
* display tasks
* add new tasks
* set tasks as completed
* remove index task
* filter task

# curl.exe -X POST -H "Content-Type: application/json" -d "{\"title\": \"Learn Flask\"}" http://127.0.0.1:5000
# curl ‐X GET http://127.0.0.1:5000

## Flask Blueprints
* organize and structure application by grouping 
  * related routes
  * templates static files
  * other code
* where are blue print used
  * structure applications into reusable components
  * organizing code into separete modules
  * enable separation of concerns by grouping related functionalities
* how to create
  * name
  * import name
  * url prefix
    * modularizing app routes
    * helpful multiple blueprints
    * 
* Task manager Application
  