# Models
from app.models.auth import Auth

# Database
from app.database.mongo import Mongo

# Flask Framework
from flask import Flask, jsonify, request, make_response



# Application
class App:


	def __init__(self):

		# MongoDB
		self.mongo = Mongo()

		# Flask Framework
		self.flask = Flask(__name__)

		# Authentication
		self.auth = Auth(self.mongo)



	# Result and http response
	def result(self, method, data):

		valid = self.auth.verify(request.headers.get('authorization'))


		if valid:

			if data:

				if '_id' in data:

					data.pop('_id')

				return self.response({'message': 'Ok', 'result': data}, 200)

			else:

				return self.response({'message': 'Not found'}, 404)

		else:

			return self.response({'message': 'Unauthorized'}, 401)




	# Response
	def response(self, data, status):

	    if data and status:

	        data['status'] = status

	        return make_response(jsonify(data), status)



	def generatetoken(self):

		return self.auth.createtoken(bytes('eubgitnh93578tghf8j93m4bh4035juh6y8y5j3q', 'utf-8'), bytes(str({"id":1,"domain":"example.com","exp":12345678765}), 'utf-8'))