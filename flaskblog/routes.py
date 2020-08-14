from flask import Flask, redirect, url_for, request, render_template, session, escape, flash
from flaskblog import app, db, bcrypt
from flaskblog.forms import LoginForm, SignupForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()

    # Check if validators are successfully
    if form.validate_on_submit():
        # Get Information from database
        user = User.query.filter_by(username=form.username.data).first()
        # Check if User and password exists in database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            # Make sure that we jump to the correct page after we login, if we come frome a login required page 
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Adds form data to database
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/dashboard', methods = ['POST', 'GET'])
# Make sure that we logged in here before access this page.
@login_required
def dashboard():
    return render_template('dashboard.html')