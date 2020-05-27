# Flask

Flask is a microframework written in Python that helps us handle requests to our website. Basically, we will be using flask to tell what to do when someone tries to access a particular endpoint to our website. 

The last part of the above sentence, someone trying to access an endpoint is a vague way of saying - a user sending an HTTP request to our website.
HTTP: HyperText Transfer Protocol is a system that the internet uses to interact and communicate between computers and servers. Whenever a user sends an HTTP request to our website, our website needs to be configured in such a way that it expects someone to access that endpoint through some method and we need to give it what it needs through what's known as an HTTP response.

Simply put, someone sends wants to see our website (HTTP request), and it gets back a response (HTTP response) that the user sees in his browser.

Figuring out what requests we might get and giving back appropriate responses to those requests is called server-side programming and that's what we are going to do with the help of Flask.



__You store your flask code in a file named "app.py"__

In the app.py, we first import the Flask class from the flask library that someone else wrote for us to use

```python
from flask import Flask
```

Instantiate a new web application called `app`, with `__name__` representing the current file

```python
app = Flask(__name__)
```

Now comes how we deal with what to reply with for a certain endpoint:
> For homepage, we represent it with just a forward slash - "/" 

We define decorators so that we can execute a function just below it that returns something when a user accesses a particular endpoint

```python
@app.route("/")
def index():
	return "Hey yo, wazzaaa(p) daawgg?"
```

That's our tiny little app that knows how to deal with one endpoint.

Now, all you have to do is go into the directory where your app.py sits, and there you can run ```flask run``` and it starts running on a local server.