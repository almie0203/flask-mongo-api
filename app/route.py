# App
from app.app import App


# Instantiate App
app = App()

# API Database
api = app.mongo.api



# Route
def route():

    return app.flask


# Handle not found error
@app.flask.errorhandler(404)
# Not Found
def not_found(e):

    return app.response({'message': 'Not found'}, 404)




# Handle method not allowed error
@app.flask.errorhandler(405)
# Not Allowed
def not_allowed(e):

    return app.response({'message': 'Method Not Allowed'}, 405)




# Set record
@app.flask.route('/<string:name>', methods=['POST'])
# Set single record
def set_record(name):

    return app.result('POST', api.insert(name, app.request.json))




# Get Records
@app.flask.route('/<string:name>', methods=['GET'])
# Get records with the limit of 20
def get_records(name):

    return app.result('GET', api.select(name))




# Get Record
@app.flask.route('/<string:name>/<int:id>', methods=['GET'])
# Get single record by id
def get_record(name, id):

    return app.result('GET', api.select(name, {'id': id}))




# Update Record
@app.flask.route('/<string:name>/<int:id>', methods=['PUT'])
# Update single record by id
def update_record(name, id):

    return app.result('GET', api.update(name, {'id': id}))




# Delete record
@app.flask.route('/<string:name>/<int:id>', methods=['DELETE'])
# Delete single record by id
def delete_record(name, id):

    return app.result('GET', api.delete(name, {'id': id}))