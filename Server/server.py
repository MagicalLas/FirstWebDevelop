from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/project')
def index_():
    return 'This is FWD Project'


@app.route('/main')
def main_page():
    return '<h1>MAIN PAGES</h1>'


if __name__ == '__main__':
    app.run()
