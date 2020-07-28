from flask import Flask, redirect, url_for, request, render_template, session, escape
from flaskblog import app
from flaskblog.forms import LoginForm, SignupForm


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
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = SignupForm()
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