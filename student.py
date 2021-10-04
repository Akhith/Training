import json
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
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


#get all the student details
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

#insert new student details
@app.route('/add_student/', methods=['POST'])
def add_student():
    try:
        if request.method in ['POST']:
            # id = Student.id
            id = request.args.get('id')
            name = request.args.get('name')
            age = request.args.get('age')
            marks = request.args.get('marks')
            print(id)
            new_student = Student (id = id,name = name,marks = marks,age = age)
            print(new_student)
            db.session.add(new_student)
            
            db.session.commit()
            return Response(json.dumps({"message":"Data inseted successfully"}), 200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)
   
# delete student details by id
@app.route('/delete_student/', methods=['DELETE'])
def delete_student():
    try:
        if request.method in ['DELETE']:
            id = request.args.get('id')
            marks = request.args.get('name')
            print(id)
            db.session.delete(Student.query.get(id))
            db.session.commit()
            return Response(json.dumps({'message': "data deleted"}),200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)

# update marks by id
@app.route('/update_student/', methods=['PUT'])
def update_student():
    try:
        if request.method in ['PUT']:
            id = request.args.get('id')
            marks = request.args.get('marks')
            updata_stud = Student.query.get(id)
            updata_stud.marks = marks
            db.session.commit()
            return Response(json.dumps({'message': "data updated"}),200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)


## find the second largest marks student deatails
@app.route('/second_student/',methods=['GET'])
def second_student():
    # for stud in Student:
    try:
        if request.method in ['GET'] :
            result = []
            user=Student.query.order_by(desc(Student.marks)).all()
            for stud in user:
                result.append({"id":stud.id,"name":stud.name,"marks":stud.marks,"age":stud.age})
                
            return Response(json.dumps({"data":result[1]}), 200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)


if __name__ == "__main__":
    app.run(debug = True)
