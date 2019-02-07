#!/usr/bin/env python

# Import
from app.api import api

# REST API
api = api()

# Run the App
if __name__ == '__main__':

    api.run(debug=True, port=100)