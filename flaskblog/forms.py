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
                                Email,
                                ValidationError)
from flaskblog.models import User

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

    # Checks if username already exists in Database
    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Benutzername existiert bereits!')

    # Checks if email already exists in Database  
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-Mail Adresse existiert bereits!')

