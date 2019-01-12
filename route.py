from flask import Flask, request, jsonify, abort

from pymongo import MongoClient


app = Flask(__name__)



client = MongoClient('mongodb://localhost:27017/')

db = client['sendtics']



tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
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
    
    task = [task for task in tasks if task['id'] == id]

    if len(task) == 0:

        abort(404)

    return jsonify({'task': task[0]})




# Run the App
if __name__ == '__main__':

    app.run(debug=True, port=100)