'''
MODELS.py
'''
from flask_sqlalchemy import SQLAlchemy
from astrologyapp import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from astrologyapp import login_manager

db=SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key= True)
    username= db.Column(db.String(150), nullable=False)
    email= db.Column(db.String(150), unique=True, nullable=False)
    password= db.Column(db.String(256), nullable=False)

    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password= self.set_password(password)

    def __repr__(self):
        return "{} has been created".format(self.username)
    
    def set_password(self, password):
        self.pw_hash= generate_password_hash(password)
        return self.pw_hash
    
    def check_password(self,password):
        return check_password_hash(self.pw_hash. password)


#Start code here for request form
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(120), unique=True, nullable=False)
    first_name=db.Column(db.String(120))
    last_name=db.Column(db.String(120))
    card_select=db.Column(db.String(120))
    comment= db.Column(db.String(550))

    