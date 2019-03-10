import time
import json
import hmac
import base64
import random
import hashlib
import datetime






# Authentication
class Auth:


	def utf8(self, data):

		return str(data.decode('utf8').replace('=', ''))



	# Signature with HMACSHA256
	def sign(self, key, payload):

		return self.encode(hmac.new(bytes(key, 'utf8'), bytes(payload, 'utf8'), hashlib.sha256).hexdigest())



	# Base64 Encode
	def encode(self, data):

		return self.utf8(base64.b64encode(bytes(str(data), 'utf8')))



	# Base64 Decode
	def decode(self, data):

		try:
			
			return self.utf8(base64.b64decode(data +'=='))

		except Exception as e:
			
			return False



	# Random String
	def random(self, length):

		o = ''

		for i in range(length):

			o += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

		return str(o)




	# Parse token
	def parse(self, auth):

		t = str(auth).replace('Bearer ', '')

		# Decode
		d = self.decode(t[32:len(t)-118])
		s = self.decode(t[-118:len(t)-32])
		
		if d and s:

			try:

				return {'token': t, 'signature': s, 'payload': json.loads(d.replace("\'", "\""))}

			except Exception as e:
				
				return



	# Verify Token
	def verify(self, secret, payload, signature):

		if payload['exp'] > time.time():
			# Remake the signature
			s = self.decode(self.sign(secret, str(payload)))
			# Compare two signature if its correct
			if s and hmac.compare_digest(signature, s):

				return True

			return {'error': 'Invalid token'}

		else:

			return {'error': 'Expired token'}



	# Token Expiration
	def expiration(self, exp = False):

		today = datetime.datetime.now()

		if 'days' not in exp:

			exp['days'] = 0

		if 'hours' not in exp:

			exp['hours'] = 0

		if 'minutes' not in exp:

			exp['minutes'] = 0


		return time.mktime((today + datetime.timedelta(minutes=exp['minutes'], hours=exp['hours'], days=exp['days'])).timetuple())




	# Create Token
	def createtoken(self, key, payload):

		return self.random(32) + self.encode(str(payload)) + self.sign(key, str(payload)) + self.random(32)