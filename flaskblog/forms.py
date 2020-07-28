from flask_wtf import FlaskForm
from wtforms import (
                    StringField, 
                    TextField, 
                    SubmitField, 
                    PasswordField)
from wtforms.validators import (
                                DataRequired, 
                                Length,
                                EqualTo,
                                Email)

class LoginForm(FlaskForm):

    username = StringField('username', [
        DataRequired()])
    password = PasswordField('password', [
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):

    email = StringField('Email', [
        Email(),
        DataRequired()
        ])

    username = StringField('username', [
        DataRequired()
            ])

    password = PasswordField('passwort', [
        DataRequired()
            ])

    confirmPassword = PasswordField('Passwort bestätigen', [
            EqualTo('password'),
            DataRequired()
            ])

    submit = SubmitField('abschicken')

