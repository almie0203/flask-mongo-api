


class api:

	def __init__(self, mongo, auth):

		# Auth
		self.auth = auth

		# API Database
		self.api = mongo['api']



	# Read Record
	def read(self, name, arg=False):

		if arg:

			return self.api[name].find_one(arg['query'])

		else:
	
			items = []

			for item in self.api[name].find():

				item.pop('_id')

				items.append(item)
			
			return items




	# Create Record
	def create(self, name, arg=False):

		if arg:

			co = self.api[name]

			id = arg['id'] = co.count() + 1

			if co.insert_one(arg):

				return co.find_one({'id': id})




	# Update
	def update(self, name, arg):

		co = self.api[name]

		if co.update_one(arg['query'], {'$set': arg['data']}).matched_count > 0:

			return co.find_one(arg['query'])




	# Delete
	def delete(self, name, arg=False):

		co = self.api[name]

		if not co.delete_one(arg['query']):

			return