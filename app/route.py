# App
from app.app import App


# Instantiate App
app = App()



# Route
def route():

    return app.flask


# Handle not found error
@app.flask.errorhandler(404)
# Not Found
def notfound(e):

    return app.response({'message': 'Not found'}, 404)




# Handle method not allowed error
@app.flask.errorhandler(405)
# Not Allowed
def notallowed(e):

    return app.response({'message': 'Method Not Allowed'}, 405)




# Get Records
@app.flask.route('/<string:name>', methods=['GET'])
# Get records with the limit of 20
def getrecords(name):

    return app.result('read', name)




# Set record
@app.flask.route('/<string:name>', methods=['POST'])
# Set single record
def setrecord(name):

    return app.result('create', name, app.request.json)




# Get Record
@app.flask.route('/<string:name>/<int:id>', methods=['GET'])
# Get single record by id
def getrecord(name, id):

    return app.result('read', name, {'query': {'id': id}})




# Update Record
@app.flask.route('/<string:name>/<int:id>', methods=['PUT'])
# Update single record by id
def updaterecord(name, id):

    return app.result('update', name, {'query': {'id': id}, 'data': app.request.json})




# Delete record
@app.flask.route('/<string:name>/<int:id>', methods=['DELETE'])
# Delete single record by id
def deleterecord(name, id):

    return app.result('delete', name, {'query': {'id': id}})