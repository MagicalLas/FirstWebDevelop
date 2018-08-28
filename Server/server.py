from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/project')
def index_():
    return 'This is FWD Project'

if __name__ == '__main__':
    app.run()
