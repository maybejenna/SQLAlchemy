"""Seed file to make sample data for blogly db."""

from app import app
from models import db, Users

# Wrap database operations with app context
with app.app_context():
    # Drop all tables
    db.drop_all()
    # Create all tables
    db.create_all()

    # If table isn't empty, empty it
    Users.query.delete()

    # Add users
    user1 = Users(username='user1', first_name='First1', last_name='Last1',)
    user2 = Users(username='user2', first_name='First2', last_name='Last2', img_url='images/user2img.png')
    user3 = Users(username='user3', first_name='First3', last_name='Last3',)

    # Add new objects to session, so they'll persist
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit--otherwise, this never gets saved!
    db.session.commit()