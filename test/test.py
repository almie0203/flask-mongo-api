from flask import Flask, request, jsonify
from pymongo import MongoClient




mo = MongoClient('localhost', 27017)

db = mo['sendtics']



user = db.users.find_one({'id': 1})


print({'result': user})


