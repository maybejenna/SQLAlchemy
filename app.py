"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Wrap the db.create_all() call with app.app_context()
with app.app_context():
    db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """List users and show add form."""
    return "<p> Welcome. It's Working</p> "


@app.route("/users")
def list_users():
    """List users and show add form."""

    users = Users.query.all()
    return render_template("list.html", users=users)
