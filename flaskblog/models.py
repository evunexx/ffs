from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

# This callback is used to reload the user object from the user ID stored in the session. 
# It should take the unicode ID of a user, and return the corresponding user object.
@login_manager.user_loader
def load_user(user_id):
    return Appuser.query.get(int(user_id))

# Need to change the name of the table, because User is a reserved word in psql
class Appuser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_filename = db.Column(db.String, default=None, nullable=False)
    image_url = db.Column(db.String, default=None, nullable=False)    
    appuser_id = db.Column(db.Integer, db.ForeignKey('appuser.id'), nullable=False)
