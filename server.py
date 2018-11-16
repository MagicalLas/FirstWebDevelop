from flask import Flask, flash, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__, template_folder="Client/doc",
            static_folder="Client/static")

@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
