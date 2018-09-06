from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run()
