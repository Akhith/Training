import json
from flask import Flask, request, jsonify, Response

from flask_sqlalchemy import SQLAlchemy
from flask import make_response




#conn="pymysql+mysqlconnector://root:root123@localhost/training"
app = Flask(__name__)

app.config['SECRET_KEY']='YOURSECRETKEY'
#app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://newroot:newroot123@localhost/training"

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    marks = db.Column(db.Integer)
    age = db.Column(db.Integer)

# db.drop_all()
db.create_all()


@app.route('/',methods=['GET'])
def show_all():
    # for stud in Student:
    try:
        if request.method in ['GET'] :
            result = []
            user=Student.query.all()
            for stud in user:
                result.append({"id":stud.id,"name":stud.name,"marks":stud.marks,"age":stud.age})
            #print(result.id)
            return Response(json.dumps({"data":result}), 200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)


# def get():
#     cur = mysql.connect().cursor()
#     cur.execute('''select * from training.Student''')
#     r = [dict((cur.description[i][0], value)
#                 for i, value in enumerate(row)) for row in cur.fetchall()]
#     return jsonify({'myCollection' : r})

if __name__ == "__main__":
    app.run(debug = True)
