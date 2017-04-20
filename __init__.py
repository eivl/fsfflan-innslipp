#!/usr/bin/env python3
# -*- coding: utf-8 -*
from flask import Flask, render_template, send_from_directory, jsonify
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
    query_floor_with_all = "SELECT FP.*, FT.*, T.id, T.ticket_code, T.holder_name, T.holder_mail from floorplan FP left join floortypes FT on FP.type = FT.id left join tickets T on FP.ticket = T.id;"
    query_string = "SELECT * from tickets"
    cursor.execute(query_floor_with_all)

    data = cursor.fetchall()

    conn.close()
    return render_template('db.html', data=data)
    # return jsonify(data=data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
