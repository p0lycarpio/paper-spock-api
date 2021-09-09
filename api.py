from flask import Flask, request
from flask_restx import Resource, Api
from pierre_spock import game

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/plus_one/<x>')
@api.doc(params={"x": "Must be an integer"})
class PlusOne(Resource):
    def get(self, x):
        result = game(x)
        return result

@api.route('/square/')
@api.doc(params={"x": "Must be an integer"}, location="query")
class Square(Resource):
    def get(self):
        x = int(request.args.get('x', 0))
        result = game(x)
        return result


if __name__ == '__main__':
    app.run(debug=True)
