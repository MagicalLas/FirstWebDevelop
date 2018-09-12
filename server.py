from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__, template_folder="Client/doc")
app.secret_key = 'Literally secret'


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/user/<name>')
def index_when_signed_in(name):
    return render_template('home.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Login Failed.'
        else:
            flash('Login Success!')
            return redirect(url_for('index'))
    return render_template('sign_in.html', error=error)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/gallery')
def gall():
    return render_template('gallery.html')

@app.route('/stat')
def stat():
    return render_template('stat.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html'), 500

if __name__ == '__main__':
    app.run()
