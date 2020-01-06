from flask import Blueprint
from App.model import db
from App.model import User
first = Blueprint("first",__name__)

@first.route("/")
def index():
    return "Index!"

# @first.route("/createdb/")
# def createdb():
#     db.create_all()
#     return "create db"

@first.route("/adduser/")
def add_user():
    user = User()
    user.name = "hahah"
    user.title = "test"
    user.save()
    return "Add user"