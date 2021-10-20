from flask import Flask
from flask_restful import Resource, Api
from resources.pokemon import Pokemon

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon, '/Pokemon', '/Pokemon/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)