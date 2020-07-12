
from db import db

class ItemModel(db.Model):
    __tablename__= 'items' #for mapping objects to the DB, we first define a table, define its columns. only the object values that match the columns will be mapped in DB


    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id= db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id= store_id

    def json(self):
        return {'name': self.name, 'price': self.price}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #same as selecting the row by name, and takingthe first row from the results
        # SQLAlchemy returns the result of DB search as an object of  class in which query is executed



    def save_to_db(self): #inserts and updating the data
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
