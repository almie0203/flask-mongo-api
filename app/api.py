# Author: Ruel Mindo

# Import
from flask import Flask, make_response, request, jsonify
from pymongo import MongoClient

# Instantiate
flask = Flask(__name__)
mongo = MongoClient('localhost', 27017)['api']




# Run the App
def api():

    return flask



# Result and http response
def result(method, data):

    if data:

        if method == request.method:

            if '_id' in data:
                
                data.pop('_id')

            return response({'result': data, 'message': 'Ok'}, 200)

        else:

            return response({'message': 'Method Not Allowed'}, 405)

    else:

    	return response({'message': 'Not found'}, 404)




# Handle not found error
@flask.errorhandler(404)
# Response
def notfound(e):

    return result('GET', False)




# Response
def response(data, status):

    if data and status:

        data['status'] = status
        
        return make_response(jsonify(data), status)




# Get All Collections
@flask.route('/<string:name>', methods=['GET'])
# Get collection from database and display
def getCollections(name):
	
	items = []

	for item in mongo[name].find():

		item.pop('_id')

		items.append(item)
	
	return result('GET', items)




# Set Collection
@flask.route('/<string:name>', methods=['POST'])
# Add collection to the database and display
def setCollection(name):

    co = mongo[name]

    id = request.json['id'] = co.count() + 1

    if co.insert_one(request.json):

        return result('POST', co.find_one({'id': id}))




# Get single collection by id
@flask.route('/<string:name>/<int:id>', methods=['GET'])
# Get collection from database and execute
def getCollection(name, id):

    return result('GET', mongo[name].find_one({'id': id}))
