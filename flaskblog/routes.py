from flask import Flask, redirect, url_for, request, render_template, session, escape, flash, jsonify
from flaskblog import app, db, bcrypt, images
from flaskblog.forms import LoginForm, SignupForm, PostForm
from flaskblog.models import Appuser, Post
from flask_login import login_user, current_user, logout_user, login_required
import datetime


@app.route('/login', methods = ['POST', 'GET'])
def login():
    login_form = LoginForm()
    # Check if validators are successfully
    if login_form.validate_on_submit():
        # Get Information from database
        user = Appuser.query.filter_by(username=login_form.username.data).first()
        # Check if User and password exists in database
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            # Make sure that we jump to the correct page after we login, if we come frome a login required page 
            #next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('dashboard'))
            return redirect(url_for('dashboard'))
        else:
            flash('Login nicht erfolgreich. Bitte prüfe dein Username oder Passwort', 'danger')


    register_form = SignupForm()
    return render_template(
    'login.html', 
    login_form = login_form,
    register_form = register_form,
    )

@app.route('/view', methods = ['POST'])
def view():
    register_form = SignupForm()
    if request.method == 'POST':
        if register_form.validate():
            hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
            user = Appuser(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
            # Adds form data to database
            db.session.add(user)
            db.session.commit()
            return 'ok'    
        return jsonify(register_form.errors), 400

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/post/new', methods = ['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        filename = images.save(form.training_image.data)
        file_url = images.path(filename)
        post = Post(
            training_title = form.training_title.data, 
            date_posted = datetime.datetime.now(),
            image_filename = filename,
            image_url = file_url,
            author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Dein Training wurde erfolgreich eingereicht', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create_post.html', form=form)

@app.route('/dashboard', methods = ['POST', 'GET'])
# Make sure that we logged in here before access this page.
#@login_required
def dashboard():
    return render_template('dashboard.html')