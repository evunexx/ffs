from flask_wtf import FlaskForm
from wtforms import (
                    StringField, 
                    TextField, 
                    SubmitField,
                    TextAreaField,
                    PasswordField)
from wtforms.validators import (
                                DataRequired, 
                                Length,
                                EqualTo,
                                Email,
                                ValidationError)
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flaskblog.models import Appuser

class LoginForm(FlaskForm):

    username = StringField('username', [
        DataRequired()])
    password = PasswordField('password', [
        DataRequired(message="Please enter a password")])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):

    email = StringField('Email', [
        Email(message='Ungültige Email Adresse!'),
        DataRequired()
        ])

    username = StringField('username', [
        DataRequired()
            ])

    password = PasswordField('passwort', [
        DataRequired()
            ])

    confirmPassword = PasswordField('Passwort bestätigen', [
            EqualTo('password', message='Passwort bestätigen stimmt nicht mit Passwort überein!'),
            DataRequired()
            ])

    submit = SubmitField('abschicken')

    # Checks if username already exists in Database
    def validate_username(self, username):

        user = Appuser.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Benutzername existiert bereits!')

    # Checks if email already exists in Database  
    def validate_email(self, email):

        user = Appuser.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-Mail Adresse existiert bereits!')

class PostForm(FlaskForm):
    
    training_title = StringField('Training', validators= [DataRequired()])
    training_image = FileField('Foto')
    submit = SubmitField('Abschicken')
