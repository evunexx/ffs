from flask.ext.wtf import Form 
#from flask_wtf import FlaskForm
from wtforms import (
                    StringField, 
                    TextField, 
                    SubmitField, 
                    PasswordField)
from wtforms.validators import (
                                DataRequired, 
                                Length,
                                Email,
                                EqualTo)

class LoginForm(FlaskForm):

    username = StringField('Name', [
        DataRequired()])
    password = PasswordField('Name', [
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):

    username = StringField('Username', 
                    validators= [DataRequired(),
                                Length(min=2 max=20)])
    email = StringField('Email',
                    validators= [DataRequired(),
                                Email()])
    password = PasswordField('Passwort',
                    validators= [DataRequired()])
    confirm_password = PasswordField('Passwort bestätigen',
                    validators= [DataRequired(), 
                                EqualTo('password')])
    submit = SubmitField ('Abschicken')
    


