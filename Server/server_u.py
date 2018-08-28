from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home'

@app.route('/login')
def login():
    return 'Login'

@app.route('/info')
def info():
    return 'info'

@app.route('/gallery')
def gall():
    return 'gallery'

@app.route('/stat')
def stat():
    return '통계'

if __name__ == '__main__':
    app.run()
