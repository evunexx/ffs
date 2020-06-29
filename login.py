from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success_login(name):
    return 'Willkommen %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success_login', name = user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success_login', name = user))

if __name__ == '__main__':
   app.run(debug = True)   
