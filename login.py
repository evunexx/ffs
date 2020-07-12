from flask import Flask, redirect, url_for, request, render_template, session, escape
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from forms import LoginForm, RegisterForm
import time

app = Flask(__name__)
app.secret_key = "foobar"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', user=username)
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('dashboard'))

    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    user = session['username']
    #form = LoginForm()
    #if request.method == 'POST':
        #session['username'] = form.username.data
        #user = form.username.data
    return render_template('dashboard.html', user = user)
    
if __name__ == '__main__':
   app.run(debug = True)   
