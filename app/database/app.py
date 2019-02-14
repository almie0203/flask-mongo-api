


class app(object):

	def __init__(self, mongo):

		# App Database
		self.app = mongo['app']



	def user(self, uid):

		data = self.app['users'].find_one({'id': 1})

		if '_id' in data:
			
			data.pop('_id')

		return data


