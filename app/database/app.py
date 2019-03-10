


class app(object):

	def __init__(self, mongo, auth):

		# Auth
		self.auth = auth

		# App Database
		self.app = mongo['app']


	def user(self, uid):

		data = self.app['users'].find_one({'id': uid})

		if '_id' in data:
			
			data.pop('_id')

		return data




	def generatetoken(self, uid, exp = False):

		user = self.user(uid)

		payload = {
			"id": user['id'],
			"domain": user['domain'],
			"exp": self.auth.expiration(exp)
		}

		return self.auth.createtoken(user['secret'], payload)




	def datetimeformat(self, exp, format = '%D %H:%M'):

		return time.strftime(format, time.localtime(exp))



	def createcollection(self, domain, endpoint):

		self.app.create_collection(self.auth.encode(domain) +'.'+ self.auth.encode(endpoint))


