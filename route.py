from flask import Flask, request, jsonify, abort

from pymongo import MongoClient


app = Flask(__name__)



client = MongoClient('mongodb://localhost:27017/')

db = client['sendtics']



data = [
    {
        'id': 1,
        'title': 'Title 1'
    },
    {
        'id': 2,
        'title': 'Title 2'
    }
]


# Get All Collections
@app.route('/collection', methods=['GET'])
# Get collection from database and display
def getCollections():

    return jsonify()




# Set Collection
@app.route('/collection', methods=['POST'])
# Add collection to the database and display
def setCollection():

    return jsonify(request.get_json())




# Get Single Collection
# Display single collection by id
@app.route('/collection/<int:id>', methods=['GET'])
# Get collection from database and execute
def getCollection(id):
    
    item = [item for item in data if item['id'] == id]

    if len(item) == 0:

        abort(404)

    return jsonify({'item': item[0]})




# Run the App
if __name__ == '__main__':

    app.run(debug=True, port=100)