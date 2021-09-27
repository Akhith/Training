from flask import Flask
from flask import jsonify
from flask import make_response
import json


app=Flask(__name__)

@app.route('/<num>')
def factorial(num):
	try:
		num1=int(num)
		fact=1
		while ( num1 > 0):
			fact= fact * num1
			num1-=1
		return make_response(f"factorial {fact}",200)
		
	except:
				
		return make_response(json.dumps("message enter a number"),404)

