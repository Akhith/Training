
from application import create_app


#conn="pymysql+mysqlconnector://root:root123@localhost/training"
app = create_app()



if __name__ == "__main__":
    app.run(debug = True)
