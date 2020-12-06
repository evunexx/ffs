from flask import Flask, redirect, url_for, request, render_template, session, escape, flash, jsonify
from flaskblog import app, db, bcrypt
from flaskblog.forms import LoginForm, SignupForm, PostForm
from flaskblog.models import Appuser, Post
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import create_engine
from werkzeug.utils import secure_filename
import os
import urllib.request
import datetime


eng = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
con = eng.connect()

#Utils (Maybe outsource Later)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# --------

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

@app.route('/view/register', methods = ['POST'])
def view_register():
    register_form = SignupForm()
    if request.method == 'POST':

        if register_form.validate():
            hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
            user = Appuser(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
            # Adds form data to database
            db.session.add(user)
            db.session.commit()
            resp = jsonify({'message': 'success'})
            resp.status_code = 201
            return resp

        return jsonify(register_form.errors), 400
        
@app.route('/view/login', methods = ['POST'])
def view_login():
    login_form = LoginForm()
    if request.method == 'POST':
        
        if login_form.validate():
            # Get Information from database
            user = Appuser.query.filter_by(username=login_form.username.data).first()

            # Check if User and password exists in database
            if user and bcrypt.check_password_hash(user.password, login_form.password.data):
                login_user(user)
                # Make sure that we jump to the correct page after we login, if we come frome a login required page 
                #next_page = request.args.get('next')
                #return redirect(next_page) if next_page else redirect(url_for('dashboard'))
                resp = jsonify({'message': 'success'})
                resp.status_code = 201
                return resp
            else:
                res.status_code = 400

        return login_form.errors
        #return jsonify(login_form.errors), 400

        

@app.route('/process', methods = ['POST'])
def process():
    post_form = PostForm()
    upload_errors = {}
    upload_done = False
    form_validate_done = False
    if post_form.validate():
        form_validate_done = True
    
    # Access file make sure datatype is valid
    file = request.files['training_image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        upload_done = True
    else:
        upload_errors['datatype'] = file.filename.rsplit('.', 1)[1].lower()
    
    if upload_done and form_validate_done:
        resp = jsonify({'message': 'Files successfully uploaded'+ file.filename})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(
            {**upload_errors, **post_form.errors}
            )
        resp.status_code = 400
        return resp

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
    rs = con.execute('''
    select 
      username,
      count,
      rank () over (
        order by count desc
      ) rank 
    from 
      user_post_count ''')
    results = rs.fetchall()
    return render_template('dashboard.html', results=results)

@app.route('/history', methods = ['POST', 'GET'])
def history():
    posts = Post.query.all()
    return render_template('history.html', posts=posts)