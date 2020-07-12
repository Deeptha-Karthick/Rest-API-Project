
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource): #Every resource has to be a class, Student is a resource since it inherits from REsource and modifies its parameters
#evevry method under the resource has the same signature ie ssame parameters

    parser= reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required= True,
    help="This field cannot be left blank")
    parser.add_argument('store_id',
    type=int,
    required= True,
    help="This field cannot be left blank")



    @jwt_required() #authenticates before we can perfron get
    def get(self, name): #get method
        item= ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}, 404


    def post(self, name): #get method This is a CRUD API ...Create Read Update

        if ItemModel.find_by_name(name):
            return {'message': "'{}' already exists".format(name)}, 400 #Users mistake
        data= Item.parser.parse_args()
        #data= request.get_json() #json we are sendinghas only price, name is sent in url
        item=ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()

        except:
            return {'message': "Error Occured"}, 500 #internal server error
        return item.json(), 201



    def delete(self, name):

        item= ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': "Item Deleted"}

    def put(self, name):


        data= Item.parser.parse_args()
        item= ItemModel.find_by_name(name)


        if item is None:
            item=ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()



class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
