import json
import hmac
import base64
import random
import hashlib






# Authentication
class Auth:


	def __init__(self, mongo):

		self.app = mongo.app


	def utf8(self, data):

		return str(data.decode('utf-8').replace('=', ''))


	def sign(self, key, payload):

		return self.encode(hmac.new(key, payload, hashlib.sha256).hexdigest().encode('utf-8'))


	def encode(self, data):

		return self.utf8(base64.b64encode(data))


	def decode(self, data):

		try:
			
			return self.utf8(base64.b64decode(data+'=='))

		except Exception as e:
			
			return False


	def random(self, length):

		o = ''

		for i in range(length):

			o += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

		return str(o)




	def verify(self, auth):

		b = str(auth).replace('Bearer ', '')

		# Payload
		p = self.decode(b[32:len(b)-118])

		if p:

			p = json.loads(p.replace("\'", "\""))


			if 'id' in p:

				u = self.app.user(p['id'])

				if b == u['token']:

					# Remake signature from received token
					s = self.decode(self.sign(bytes(u['secret'], 'utf-8'), bytes(str(p), 'utf-8')))

					if s:
							
						# Compare two signature if its correct
						if hmac.compare_digest(self.decode(b[-118:len(b)-32]),s):

							return p




	def createtoken(self, key, payload):

		return self.random(32) + self.encode(payload) + self.sign(key, payload) + self.random(32)