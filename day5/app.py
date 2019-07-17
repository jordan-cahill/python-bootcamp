from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'sogeti'   # generally this would be hidden
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates '/auth' endpoint

items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank'
    )

    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

        return {'item': None}, 404 # not found

    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'message': f'An item with name {name} already exists'}, 400 # bad request

        # data = request.get_json()
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # created

    def patch(self, name):
        data = Item.parser.parse_args()

        for item in items:
            if item['name'] == name:
                item.update(data)
                return item

                #del items[item.index()]    would be a put
                #items.append(item)
        
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # created

class ItemList(Resource):

    def get(self):
        return {'items': items}

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)