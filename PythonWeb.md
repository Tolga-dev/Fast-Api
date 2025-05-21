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
* filter taskE

# curl.exe -X POST -H "Content-Type: application/json" -d "{\"title\": \"Learn Flask\"}" http://127.0.0.1:5000
# curl -X GET http://127.0.0.1:5000

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
  * django has orm 
  * flask not, uses sql alc
  * flask no have admina panel, django has
  * do get do post
    * server side, how get and post request are to be processed on the server side
  * flask has, bulit in server web
  * jinja2 templating engine that allows you to build dynamic html pages
  * first argument in flask
    * reserved arguments, always be same, as file name, where flask app is defines


# Authorization and Authentication

## Term

hash functions
* md5
* sha1
* sha2
* they re not perfect and make collisions
hash collision
* when two distinct pieves of data in same hash value
salt
* hashed passwords (typically not strong passwords) are particularly v
* ulnerable to another type of attack known as a rainbow table attack.
* rainbow
    * use precomputed rainbow table to recover plain text passwords
* salt irandom data fed as an additional input to a one way function that hashes data pas
Binary to Text encoding
* important for communication channel does not allow binary data or is not 8 bit clean
* email systems
* http , support text data
* most pop is base 64
* status codes
  * 200 OK: The request was successful, and the server has returned the requested data. This is the standard response for successful HTTP requests.
  * 204 No Content: The request was successful, but the server is not returning any content in the response. This status is often used when an action has been executed but no further data needs to be sent back to the client.
  * 400 Bad Request: The server could not understand or process the request due to invalid syntax or a malformed request. This error is often caused by issues with the client's input.
  * 401 Unauthorized: The request requires user authentication. This response is given when authentication credentials are either missing or invalid, meaning the client must provide valid credentials to access the resource.
  * 403 Forbidden: The server understands the request but refuses to authorize it. This usually happens when the user does not have the necessary permissions to access the resource, even though they may be authenticated.
  * 404 Not Found: The server cannot find the requested resource. This error occurs when the server cannot locate the resource based on the provided URL or endpoint.
  * 409 Conflict: The request could not be processed because of a conflict with the current state of the resource. This typically happens when the request would cause a data inconsistency, such as a duplicate entry.
  * 501 Not Implemented: The server does not support the functionality required to fulfill the request. This status code indicates that the server does not recognize the method used or cannot complete the request with the current functionality

* concepts form the backbone of secure data handling and communication across systems.

## Authentication
* authentication 
  * act of proving an assertion, identity of a computer system user
  * process where a user provides their username, password, token, other credentials
* identification
  * process of verifying that a user exists within a system by providing an identifier, 
    * user name, email, phone number
* it plays vitol role, only authorized users can access resources
* verify identity of a user
* confirming that they are who they claim to be
* without it system is vulnerable to unauthorized access, data breaches, other security threats
* used for verifyinh other applications that interact with your application

## Authentication Types
* password based 
* token based
* MFA
* Certificate based
* api keys

## Password Based Authentication
* storing password directly is unsafe, so use sha-1
* response object is instance of make_response
* 401
  * authentication was not provided when its required
  * auth was failed
  * 

> curl.exe -X POST -H "Content-Type: application/json" -d "{\"username\": \"Bob\", \"password\": \"Qwerty123\"}" http://127.0.0.1:5000/auth/sign_up
> curl.exe -X GET http://127.0.0.1:5000/ -u Bob:Qwerty123
> curl.exe -X POST -H "Content-Type: application/json" -d "{\"title\": \"Learning Flask\"}" http://127.0.0.1:5000 -u Bob:Qwerty123

### Token Based Authentication
* user login
  * users provides their credentials
* token generation
  * server generates unique token
* token storage
  * user stores in local storage or a cookie
* request authenticated
  * user includes the token in the authorization header
* token verification
  * server verifies the token with each request to ensure the user is authenticated

* populer token generator
  * json web token
    * jwt
    * encode
      * payload
        * info must be encoded
      * key 
      * algo
        * algo for token
        * default hs256
    * decode


> curl.exe -X POST -H "Content-Type: application/json" -d "{\"username\": \"Bob\", \"password\": \"Qwerty123\"}" http://127.0.0.1:5000/auth/login
> curl.exe -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkJvYiJ9.EqXuR4FLSPsIj6Z-OcrlzVI_1yb0XtEVkX5TF61xeFw" -d "{\"title\": \"Learning Flask\"}" http://127.0.0.1:5000


## Other Authentication types
* MFA
  * multi factor authentication
  * sercurity measure that requires more than one form of verification to prove your identity
  * two factor authentication 2fa
* api key
  * simple method to secure app by requiring clients to provide unique key string 
  * not used to auth a user
  * used to verify auth of external system
  * In applications with multiple services or microservices,
  * API keys are used for secured communication between them. 
  * Services that allow third-party developers to integrate with their platforms
  * (e.g., Google Services) use API keys to grant controlled access to their services. 
  * Monitoring tools and analytics platforms use API keys to track and report API usage, errors,
  * and performance metrics.
* Here is an example how to implement API key authentication in Flask:
```python


from flask import Flask, make_response, request

app = Flask(__name__)

# API keys (in real applications, databases or environment variables are used)
api_keys = {
    "123456": "Application A",
    "abcdef": "Application B",
}

# Authentication decorator
def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("x-api-key")  # Extract API key from headers
        if not api_key or api_key not in api_keys:
            # the request cannot be authenticated
            return make_response({"message": "Unauthorized"}, 401)
        return f(*args, **kwargs)
    return decorated_function


@app.route("/public")
def public_route():
    return make_response({"message": "No API key needed."}, 200)


@app.route("/private")
@require_api_key
def private_route():
    return make_response({"message": "Valid API key was provided."}, 200)


if __name__ == "__main__":
    app.run(debug=True)
```

* certificate based authentication
  * security mechanism in which digital certificates are used to authenticate users devices system
  * digital certificate issued by a trusted certificate authority CA
    * public key and info 
  * during authentication process
    * server provides public certificate to the client
    * client verifies the server certificate to the server
    * server verifies certificate's validity and checking issuer, expiration date and whether it is still trusted
    * if all are ok, server can decrypt the message or verify digital signature using public key
      * ssl tls
      * vpn
      * enterprise system
* single sign on
  * sso
  * aithentication scheme
  * allows a user to log in with a single id to any of several related yet, independent software systems
  * keys benefits
    * users dont need to remember multiple passwords
    * saves time as users
    * reduces risk 
* common protocols and standard
  * saml
    * security assertion markup language
    * xml based open standard used for exchanging authentication and authorization data
      * between id idp, server provider sp
    * used for sso, enabling users to log in multiple apps
  * oauth 2.0 and open id 
    * modern standards used for auths 
  * keyberos
    * network auth protocol designed to provide secure authentication over insecure networks
  
# Authorization
* function of specifying access rights privileges to resources 

# Sessions and Cookies
* terms
  * a session 
    * time delimited two way link 
    * a practical later in tcp ip protocol enabling interactive expression and information
    * exchange between two or more coms 
  * http cookies
    * web cooky, internet cookie, browser cookies or simply cookies
    * are small blocks of data created by a web server while a user is browsing a website and placed on the users comp
  * sessions are server side mechanism used to store user data for specific period
  * a cookie small piece of data stored on the users device by their web browsers
  * client side
    * session data is stored directly on client's browser
    * pros
      * scalability
      * reduced server load
      * offline access
    * cons
      * security
      * data size limit
  * server side
    * stored on the server
    * unique session identifier is stored on client's browser
    * in cookie
    * pros
      * security
      * unlimited data
      * fine grained control
    * cons
      * increase server load
      * scalability challenges
      * no offline access
    * flask uses client side

```python

from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "GTYlv>K]0=otL=B`@z^s"  # some randomly generated string

@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        return f"Hello, {username}. Click <a href='{url_for('index')}'>here</a>!"
    return """
        <form method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
```

```python
from flask import Flask, make_response, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    username = request.cookies.get("username")
    if username:
        return f"Logged in as {username}"
    return "You are not logged in"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        resp = make_response(f"Hello, {username}. Click <a href='{url_for('index')}'>here</a>!")
        resp.set_cookie("username", username)
        return resp
    return """
        <form method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
    """


@app.route("/logout")
def logout():
    resp = make_response(f"Cookie is cleared! Click <a href='{url_for('index')}'>here</a>!")
    resp.delete_cookie("username")
    return resp


if __name__ == "__main__":
    app.run(debug=True)


```

```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "GTYlv>K]0=otL=B`@z^s"  # some randomly generated string

@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        return f"Hello, {username}. Click <a href='{url_for('index')}'>here</a>!"
    return """
        <form method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


```
* user preferences
  * lang 
  * theme 
  * font size
* shopping card
* user history
* localization

# Template 
* jinja2
  * modeled after django
  * fast, widely used, provides an optional sandboxed template execution env 
* mako
  * flexible, fast
  * pre processing, dynamic scripting html
  * clean separation between presentation and business
* genshi
  * generation of output for web
  * focused xml based templates
  * xml towards web based app
* django
  * powerful templating system
  * clear separation of business and presentation
  * simple syntax
  * extensible
* primarly, jijna2

```html
<!DOCTYPE html>
   <html>
   <head>
       <title>Task List</title>
   </head>
   <body>
       <h1>Tasks</h1>
       <ul>
       {% for task_id, task in tasks.items() %}
           <li>{{ task.title }} - {% if task.is_completed %}Completed{% else %}Pending{% endif %}</li>
       {% endfor %}
       </ul>
   </body>
   </html>
```
* conditional display
```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.name }}!</p>
{% else %}
    <p>Please <a href="/login">login</a> to access your dashboard.</p>
{% endif %}

```
* looping

```html
<ul>
{% for item in item_list %}
    <li>{{ item.name }} - {{ item.description }}</li>
{% endfor %}
</ul>


```

* template inheritance
* base
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
* about html
```html
{% extends "base.html" %}

{% block title %}About - My Website{% endblock %}

{% block content %}
    <h1>About Us</h1>
    <p>This is the about page.</p>
{% endblock %}
```
* including sub templates
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    {% include 'header.html' %}
    <h1>Welcome to My Website</h1>
    {% include 'footer.html' %}
</body>
</html>

```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Welcome to My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
            </ul>
        </nav>
    </header>
```
```html
    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>
</body>
</html>


```
* Using Filters
```html
<p>{{ user.bio|default('No biography provided.') }}</p>
```
* Macros
```html
{% macro render_input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}">
{% endmacro %}
```

```html
{% from "macros.html" import render_input %}

<form method="post">
    {{ render_input('username') }}
    {{ render_input('password', type='password') }}
    <button type="submit">Submit</button>
</form>
```
*  builtin-filters, custom-filters, builtin-tests, custom-tests, and global functions
1 
# Rest
## Rest software architectural style
* definition and reason to use
  * representational state transfer or rest
  * stateless
  * scalable 
  * supporting large numbers of client
  * cache responses can improve performance by reducing server load
  * not a protocol
  * architectural style
  * fuse any transport protocol and representation 
  * json over http is the most popular
* Main principles
  * client server
    * separates the ui from data storage
    * client
      * ui and user experience
    * server
      * requests, responses
  * stateless
    * visibility
    * reliability 
    * scalability
    * reused
  * cacheable
    * server
      * label reponses as cacheable
      * response can be cache, clience cache can reuse in future
  * uniform interface
    * simplifies, decouples architecture
    * four things
      * identification of resources
      * manipulation of resources
      * self descriptive messages
      * hypermedia as engine of application state hateoas
  * layered system
    * architecture of rest allows for a layered system 
  * code on demand
    * limitations
      * despite its numerous advantages rest also has some limits
        * not goodfir for real time apps
          * data needs to be pushed from the server to client in real time
        * if data size is big, stateless can fuck server
        * http can be restrictive
          * predefined semantics
        * uniform interface constraint 
        * does not inherently support transactions
          * app level
        * for complex quesries, rest api, may require mor erequests than other types of apis

# rest api best practices and naming conventions
* introduction
  * levels
    * swamp of pox plain old xml
      * at this level the services uses http as transport system for remote interactions 
      * service relies on single url and http post 
      * http as a tunnel for its own data
    * resources
      * individual resources are created on the server
      * each resource has a specific url
      * http methods are not leveraged
      * post may still be used for all crud
        * created read update del
    * http verbs
      * arch start to embrace full spectrum of http methods intended for different ops
        * get, post, put, delete
      * more efficient
      * more aligned
      * does not fullt exploit all features
    * hypermedia controls
      * hateoas, herpermedia as the engine of application state to the responses turning the app into res
      * not only date, also info
      * guiding client on possible actions from the current state
* protocol
  * in no restrictions or requirements, easy to utilize this protocol
* resource
  * data we want to manage
  * key info in rest is resource
  * rest api uses uniform resource identifiers uri to address resources
* resource types
  * category or nature of a particular resource
  * entitty noun not action verb as entities 
  * http get post put delete
    * represent the actions to be performed on these resources
  * first rule follows from this
    * use nouns for resources
    * Doc resource or singleton
      * a doc is singular concept that is like an object instance or dataabase record 
      * a specific, discrete item with its own attributes
      * retrive, update or delete a singleton resource
      * get /book/123 In this example, '123' is the unique identifier of a book document.
    * Collection resource
      * server managed directory of resources
      * clients can propose new resources to be added to a collection
      * get /books
    * store resource
      * a store resource is client managed resource repo
      * can contain other resources
      * POST /books/123/bookmarks 
      * In this example, 'bookmarks' is a store of bookmarks for a specific book. The client can create (POST) new bookmarks, and manage (DELETE, UPDATE) existing ones.
* resource naming 
  * general naming conventions for resources
    * use plural nouns
      * books not book
    * avoid uppercases
    * forward slash /
    * no trailing dont end with /
    * use hyphens
      * - not _use 
    * http
      * DELETE /api/books/{id} to delete a book, not /api/books/{id}/delete.
    * no crud functions names
      *  use POST /api/books to create a new book, not /api/books/create.
    * query params
      * use filter 
        * /api/books?author=john.
    * use path variables
      * /api/books/{id}
  * Post
    * return 201 if good
  * get
    * return 200 if good
  * put
    * 200
    * not good 404
  * delete
    * 200
    * 204 no conent
    * 202 accepted

# Orms
## Postgresql, phadmin, connection to db
* what is postgresql
  * highly stable database system that has been developed over three decades
  * reliability
  * robust feature
  * performance
* keys
  * acid
    * atomicity
    * consistency
    * isolation
    * durability
  * extensiblity
    * users can define their own data types
    * bouild out custom functions
    * even write code 
  * internationalizatoin text search
  * concurrency
    * multi version concurrency control mvcc
  * reliability
    * strong track record of arch integrity and robustness
* PGAdmin
  * Intro
    * one of ths most popular and feature rich open source admin and development platforms for postgresql
    * it allows 
      * database administrators, develoeprs and other users to interact with ui
    * meet needs of both novice and experienced posgres users
  * keys
    * user friendly
    * comprehensive dashboard
    * query tool
    * data visulazition
    * support for multiple postgresql versions
## Python db api
* working with databases in python
  * pep - 249
  * api, to ensure uniformity across pytgon modules that facilitate database access
  * create consistency
  * making modules simpler
  * uniform approach makes code transferable
  * broadens python capabilities
* sql lite databases
  * lightweight
  * file based 
  * dev and test cuz simple, ease of setup
  * c lib
* connection to database
  * 
```python
import sqlite3

conn_obj = sqlite3.connect("python_web.db")
conn_obj.close()

```

* after creating data base,
  * it is ready to open a connection to the database in python.
    * postre 
      * dat atypes are deseigned to handle a wide range of precise and large data volumes
        * suitable for complex and large scale apps
      * supports traditional data types such as int, text,  bool, json, xml, arrays
    * sqllite
      * more dynamic types
        * null, int, real, text, blob
      * not enfor type of data 
      * lightweight
      * creating
        * 
      
pip install -binary
* sql lite 
  * dynamic, int text boolean
    * not varchar or bool
* serial vs integer primary key autoincrement
  * in postgresql, serial for auto inc int columns, used for primary keys
  * in sqllite, integer primary key autoincreament, auto is default, 
* varchar vs text
  * postgresql
    * different, varchar and text
    * varchar is limited and often not set in simple cases, making it similar to text
  * sqllite, cannot different, text and varchar, all tedxt data as text
* bool vs boolean
  * postgre, bool as boolean
  * sql lite, it can be uses int to store bool val
* prim keys
  * both uses primary,
  * declaration slightly different cuz data types
* placeholders is '?', later replaced by actual value or string during the execution of sql query
  * security
  * maintainability
  * flexibility
  * performance


## Introduction to ORM and SQLAlchemy
* overview of orm
  * object relational mapping 
    * orm o/rm o/r
  * orm
    * python
    * eases translation of data between oop and relational databasee
    * manipulate databse as notmal python objects
    * abstraction layer simplifies data operations into python scripts
    * code and database a bridge link
    * crud
    * core business more time
    * libs
      * sqlalchemy
        * high performance
        * efficient database
      * django
        * robust abstraction layer
        * python code to sql
      * peeweee
        * simple, expressiviness
        * small lightweight
      * pony orm
        * use of generator expressions for crafting queries
          * complex quesries in pure python
      * sqlobject
        * provides oop 
    * why orm
      * streamlines database interactions
      * minimizes repetitive code
      * enhances code maintainability
      * facilitates cross database Compatibility
        * sql, mysql, postgresql
    * when to use orm
      * crud ops
      * handling copmlex queries
      * fast paces development
* introduction to sqlalchemy
  * db api 
    * operates behind scenes 
    * can abstract much of the complexity involved in direct database operation
    * this abstraction, developers can interact with databases in a more phythonic way 
      * without needing to write sql queries directly
  * two primary copmonents
    * oop
    * core
* definin models and sessions
  * how to define models in sqlalchemy
    * two
      * classical traditional imperative
        * explicitly specify both the table and mapper configurations
        * granular controler over mapping process 
        * simple
      * streamlined declarative
        * process more simple by enabling developers
        * table schema directly within python class
        * table and mapper setting 
  * sessions
* crud operation with sql alchemy
  * simplicity and readability
    * orm models privide a clean and readable way
  * data abstraciton
    * by abstracting the database layer, orm allows you to focus on the logical representation of data rather than the underlying database schema
  * attribute access
    * columns in database are accessible as attributes of the model
    * read and update
  * automatic transactions
    * commit these changes to database with single session.commit
  * relationship
    * sqlalchemy powerful tools for managing relations between tables, allowing you to navigate manipulate 
    *  By leveraging the features of SQLAlchemy, such as automatic transactions, relationship management, and data abstraction, developers can create robust and efficient web application
* database migrations with alembic
  * introductoin to alembix
    * mike bayer
    * to meet robust, flexible database migration tool that integrates well with sqlalchemy
    * agnostic, lightweight, allow developer to track and implement changes in the database schema over time
    * powerful, versatile
  * keys
    * version control for database schema
      * alembic is a database migration tool 
      * version control for database schema
      * enabling systematic tracking, application and reversion of shema changes
    * auto generation migration
      * auto generatees migrations scripts by comparing sqlalchemy define models
    * support for multiple databases
      * supports a wide range of sql
      * databases, postgresql, mysql, oracle sqllite
    * working with branches
    * 
      * alembic allows for the branching and merging of schema changes
      * facilitating the management of different development
      * trajectories in complex environment
  * setting up alembic in a project
  * Common pitfalls and troubleshooting
    * conflict errors
    * downgrade script issues
    * database connection errors
    * autogenerate limitations




This includes BI tools and dashboard-building platforms like

Superset
Grafana
Google Looker Studio
As well as data science tools like

Pandas
SQLAlchemy
psql
