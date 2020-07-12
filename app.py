from flask import Flask
from flask_restful import Api #REsource is something we get from user and give the user back
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SQLALCHEMY_TRACK_MODIFIATIONS'] = False
app.secret_key ='hi' #key for authentiatin
api= Api(app)

@app.before_first_request #before the first request made in our app, the below function will execute
def create_tables():
    db.create_all()

jwt= JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>') #Adding STudent as a resource and giving it a path
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    db.init_app(app) #passing our app in to be used with SQLAlchemy
    app.run(port=1000, debug=True) #debug gives u reasonable error
