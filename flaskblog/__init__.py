from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

UPLOAD_FOLDER = 'flaskblog/uploads/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

login_manager.login_view = 'login'
login_manager.login_message = 'Bitte melden sich sich an um diesen Inhalt zu sehen.'


POSTGRES = {
    'user': 'flask',
    'pw': 'tw6',
    'db': 'ffspsql',
    'host': 'localhost',
    'port': '5432',
}

# Config Application:
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'



import flaskblog.routes
