


class api(object):

	def __init__(self, mongo):

		# API Database
		self.api = mongo['api']



	# Select
	def select(self, name, arg=False):

		if arg:

			return self.api[name].find_one(arg)

		else:
	
			items = []

			for item in self.api[name].find():

				item.pop('_id')

				items.append(item)
			
			return items




	# Insert
	def insert(self, name, arg=False):

		if arg:

			co = self.api[name]

			id = arg['id'] = co.count() + 1

			if co.insert_one(arg):

				return co.find_one({'id': id})




	# Update
	def update(self, name, arg=False):

		return {}




	# Delete
	def delete(self, name, arg=False):

		return {}

