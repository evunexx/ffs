from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
POSTGRES = {
    'user': 'flask',
    'pw': 'tw6',
    'db': 'ffspsql',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)

import flaskblog.routes
