import time
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
			
			return self.utf8(base64.b64decode(data +'=='))

		except Exception as e:
			
			return False


	def random(self, length):

		o = ''

		for i in range(length):

			o += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

		return str(o)




	def parse(self, auth):

		t = str(auth).replace('Bearer ', '')

		# Decode
		d = self.decode(t[32:len(t)-118])
		s = self.decode(t[-118:len(t)-32])

		if d and s:

			return {'token': t, 'payload': json.loads(d.replace("\'", "\"")), 'signature': s}



	def verify(self, secret, payload, signature):

		if payload['exp'] > time.time():
			# Remake the signature
			s = self.decode(self.sign(bytes(secret, 'utf-8'), bytes(str(payload), 'utf-8')))
			# Compare two signature if its correct
			if s and hmac.compare_digest(signature, s):

				return True

			return {'error': 'Invalid token'}

		else:

			return {'error': 'Expired token'}




	def createtoken(self, key, payload):

		return self.random(32) + self.encode(payload) + self.sign(key, payload) + self.random(32)