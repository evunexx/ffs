from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

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
