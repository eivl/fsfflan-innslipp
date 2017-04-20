#!/usr/bin/env python3
# -*- coding: utf-8 -*
from flask import Flask, render_template, send_from_directory
from flaskext.mysql import MySQL
from mysecret import DATABASE_USER, DATABASE_PASS, DATABASE_HOST
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)


@app.route('/')
def homepage():
    return "Hei på deg!, Flask virker som det skal.."


@app.route('/m2')
def m2():
    return render_template('main.html')


@app.route('/db')
def db():
    mysql = MySQL()
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = DATABASE_USER
    app.config['MYSQL_DATABASE_PASSWORD'] = DATABASE_PASS
    app.config['MYSQL_DATABASE_DB'] = 'opascree_lan-seats'
    app.config['MYSQL_DATABASE_HOST'] = DATABASE_HOST
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    query_string = "SELECT * from tickets"
    cursor.execute(query_string)

    data = cursor.fetchall()

    conn.close()

    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
