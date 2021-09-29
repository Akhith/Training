from flask import Flask, jsonify,request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask import make_response
import json



#conn="pymysql+mysqlconnector://root:root123@localhost/training"
app = Flask(__name__)

app.config['SECRET_KEY']='YOURSECRETKEY'
#app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root123@localhost/training"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    marks = db.Column(db.Integer)
    age = db.Column(db.Integer)

@app.route('/')
def show_all():
   return make_response(json.dumps(students = Student.query.all()),200 )


# def get():
#     cur = mysql.connect().cursor()
#     cur.execute('''select * from training.Student''')
#     r = [dict((cur.description[i][0], value)
#                 for i, value in enumerate(row)) for row in cur.fetchall()]
#     return jsonify({'myCollection' : r})

if __name__ == '__main__':
    app.run()
