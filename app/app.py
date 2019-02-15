# Models
from app.models.auth import Auth

# Database
from app.database.mongo import Mongo

# Flask Framework
from flask import Flask, jsonify, request, make_response

# Date Time
import time
import datetime
import calendar




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

		token = request.headers.get('authorization')

		parse = self.auth.parse(token)

		if token and parse:

			user = self.mongo.app.user(parse['payload']['id'])

			if user and user['token'] == parse['token']:

				verify = self.auth.verify(user['secret'], parse['payload'], parse['signature'])

				if verify == True:

					if data:

						if '_id' in data:

							data.pop('_id')

						return self.response({'message': 'Ok', 'result': data}, 200)

					else:

						return self.response({'message': 'Not found'}, 404)

				else:

					return self.response({'message': verify['error']}, 401)

		
		return self.response({'message': 'Unauthorized'}, 401)




	# Response
	def response(self, data, status):

	    if data and status:

	        data['status'] = status

	        return make_response(jsonify(data), status)



	def expire(self, days = False):

		today = datetime.date.today()

		if days == False:

			days = calendar.monthrange(today.year, today.month)[1]

		return time.mktime((today + datetime.timedelta(days=days)).timetuple())




	def generatetoken(self, exp = False):

		return self.auth.createtoken(bytes('eubgitnh93578tghf8j93m4bh4035juh6y8y5j3q', 'utf-8'), bytes(str({"id":1,"domain":"example.com","exp":self.expire(exp)}), 'utf-8'))