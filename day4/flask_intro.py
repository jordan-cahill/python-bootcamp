"""FORGOT TO MENTION"""

# type hinting

def my_function(one: str, two: str, three: str):
    print(one, two, three)

my_function('hello', 'sogeti', 'austin')

# classes use Pascal case is a convention

"""WHAT IS AN API"""

# applicationn programming interface
# a software intermediary allowing 2 applications to talk to each other

# REST Web API
# allowing the website to talk to the database

# provides HTTP responses to HTTP requests
# the browser sends the request
# the api is a long running process on some server
# waiting to receive an HTTP request and will respond

# REQUEST FORMAT
# GET / HTTP/1.1 --> verb, path, protocol
# Host: www.google.com

# POST, DELETE, PUT, etc
# POST & PUT will include a JSON body in the request

# headers -- key/value pairs
# Content-Type = application/json
# Authentication tokens

# RESPONSE FORMAT
# returning JSON --> broser can do logic with this
# could send HTML --> browser can display this

# headers
# HTTP status code -- how the request went, was it handled successfully?
# if an error occured, what error?
# 200 ok
# 404 not found (path was wrong)
# 429 too many requests (come back later)

# RESPONSE DATA
# when you are making a REST API, the api will respond with a "resource"

            # endpoint --> chair is a resource
# GET       /item/chair
# POST      /item/chair
# PUT       /item/chair
# DELETE    /item/chair

# when designing your API, and thinking about waht endpoints/resources
# you should make to represent your data, you can get into an 
# objec toriented mindset becasue resources ~ objects

# REST IS STATELESS
# one request cannot depend on any other requests
# server only knows about current request

# WHY DO WE NEED AN API?

# to decouple backend and frontend
# & standardize interactions with db

# this separation allows for testing separarely
# bc the way information is displayed is inherently
# different from ensuring the proper data is received from the db

# also .. JavaScript literally cannot talk to database from
# the browser. JS can only send info to the server.

"""GETTING STARTED"""

# get into venv
# pip --version
# make sure it is python 3.7
# pip install flask


# windows
# venv\Scripts\activate

# mac
# source venv/bin/activate

from flask import Flask

app = Flask(__name__)  # name is a reference to the file you are currenlty in

@app.route('/')
def home():
    return 'Hello World!'

app.run(port=5000)