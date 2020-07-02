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

    username = StringField('Name', [
        DataRequired()])
    password = PasswordField('Name', [
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Login')


