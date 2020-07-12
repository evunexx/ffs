from flask_wtf import FlaskForm
from wtforms import (
                    StringField, 
                    TextField, 
                    SubmitField, 
                    PasswordField)
from wtforms.validators import (
                                DataRequired, 
                                Length)

class LoginForm(FlaskForm):

    username = StringField('username', [
        DataRequired()])
    password = PasswordField('password', [
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Login')


