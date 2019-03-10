# Import
from pymongo import MongoClient

# Databases
from app.database.app import app
from app.database.api import api


mongo = MongoClient('localhost', 27017)


# Mongo
class Mongo:

	def __init__(self, auth):

		self.app = app(mongo, auth)
		self.api = api(mongo, auth)