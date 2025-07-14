from flask import Flask
from markupsafe import escape

app = Flask(__name__)


# at initial open, the index page is loaded.
@app.route("/")
def index():
    return "<h1>Hello, Welcome to the Index section. Enter your name in URL. Example: /John</h1>" 


# use angular brackets for variables
@app.route("/<name>")
def name(name):
    return f"<h1>Hello, {escape(name)}. Add your favorite food. Example: /John/jalapeno</h1>"

@app.route("/<name>/<food>")
def food(name, food):
    return f"<h1>This is the last section, {name}. And, your favorite food is {food}.</h1>"

# variables can be defined by depending on the appropriate data type
#   string (default)
#   int
#   float
#   path (same with string, but with slashes /)
#   uuid

@app.route("/post/by_id/<int:post_id>")
def show_post_by_id(post_id):
    return f"<h1>The post_id you entered is {post_id}.</h1>"