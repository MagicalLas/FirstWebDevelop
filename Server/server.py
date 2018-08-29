from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/user/<name>')
def index_when_signed_in(name):
    return render_template('home.html', name=name)

@app.route('/login/')
def login():
    return render_template('sign_in.html')

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/gallery/')
def gall():
    return render_template('gallery.html')

@app.route('/stat/')
def stat():
    return render_template('stat.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/main')
def main_page():
    return '<h1>MAIN PAGES</h1>'


if __name__ == '__main__':
    app.run()
