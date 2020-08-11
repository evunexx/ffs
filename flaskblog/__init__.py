from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)

import flaskblog.routes
