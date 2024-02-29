"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Users(db.Model):
    """Users."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    username = db.Column(db.String(50),
                         nullable=False,
                         unique=True)
    first_name = db.Column(db.String(50),
                           nullable=False,
                           unique=True)
    last_name = db.Column(db.String(30), nullable=True)
    img_url = db.Column(db.String, nullable=True, default="images/default_user_img.png")

    def __repr__(self):
        """Show info about user."""
        return f"<User {self.id} {self.username} {self.first_name} {self.last_name}>"