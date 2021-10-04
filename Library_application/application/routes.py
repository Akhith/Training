import json
from flask import request, Response
from flask import current_app as app
# from application.__init__ import db
from . models import Book, db
from flask_sqlalchemy import SQLAlchemy


   #insert new student details
@app.route('/', methods=['POST'])
def add_Book():
    try:
        if request.method in ['POST']:
            # id = Student.id
            id = request.args.get('id')
            name = request.args.get('name')
            author = request.args.get('author')
            
            price = request.args.get('price')
            quantity = request.args.get('quantity')
            #print(id)
            new_book = Book (id = id,name = name,author = author,price = price,quantity = quantity,total = int(price)*int(quantity))
            # print(new_student)
            db.session.add(new_book)
            
            db.session.commit()
            return Response(json.dumps({"message":"Data inseted successfully"}), 200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)

@app.route('/show_all/',methods=['GET'])
def show_all():
    # for stud in Student:
    try:
        if request.method in ['GET'] :
            result = []
            Book_list=Book.query.all()
            for Book_record in Book_list:
                result.append({"id":Book_record.id,"name":Book_record.name,"author":Book_record.author,"price":Book_record.price,"quantity":Book_record.quantity,"total":Book_record.total})
            #print(result.id)
            return Response(json.dumps({"data":result}), 200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)

@app.route('/delete_Book/', methods=['DELETE'])
def delete_Book():
    try:
        if request.method in ['DELETE']:
            id = request.args.get('id')
    
            db.session.delete(Book.query.get(id))
            db.session.commit()
            return Response(json.dumps({'message': "data deleted"}),200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)

@app.route('/update_Book/', methods=['PUT'])
def update_Book():
    try:
        if request.method in ['PUT']:
            id = request.args.get('id')
            quantity = request.args.get('quantity')
            updata_book = Book.query.get(id)
            new_book = Book.query.filter(Book.id == id)
            updata_book.quantity = quantity
            updata_book.total = int(updata_book.quantity) * int(updata_book.price)

            db.session.commit()
            return Response(json.dumps({'message': "data updated"}),200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)


@app.route('/show_quantity/',methods=['GET'])
def show_quantity():
    try:
        if request.method in ['GET']:
            result=[]
            Book_list = Book.query.order_by(Book.quantity).all()
            for Book_record in Book_list:
                result.append({"name":Book_record.name,"price":Book_record.price,"quantity":Book_record.quantity})
            return Response(json.dumps({'data': result}),200)
        else:
            return Response(json.dumps({"message": "Data cannot be fetched"}), 400)
    except Exception as e:
         return Response(json.dumps({"message":str(e)}), 400)




   