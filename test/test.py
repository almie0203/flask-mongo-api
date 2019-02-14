import base64


encoded = base64.b64encode(bytes('Test data', 'utf-8')).decode('ascii').replace('=', '')

print(encoded)

decoded = base64.b64decode(encoded).decode('ascii')

print(decoded)
