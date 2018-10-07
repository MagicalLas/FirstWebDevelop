from flask import Flask, flash, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__, template_folder="Client/doc",
            static_folder="Client/static")
app.secret_key = 'Literally secret'

conn = sqlite3.connect("./Server/Database/Login.db", check_same_thread=False)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():

    id = request.form['id']
    password = request.form['pass']
    cur = conn.cursor()
    cur.execute("select * from User where id='"+id+"' and password = '"+password+"'")
    rows = cur.fetchall()

    if(len(rows)==0):
        return "false"
    return "true"

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    id = request.form['id']
    password = request.form['pass']
    cur = conn.cursor()
    cur.execute("insert into User values('"+name+"','"+id+"','"+password+"')")
    cur.execute("select * from User where name='"+name+"'")
    rows = cur.fetchall()

    if(len(rows)==0):
        return "false"
    return "true"

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
    app.run(host='0.0.0.0', port=5000)
