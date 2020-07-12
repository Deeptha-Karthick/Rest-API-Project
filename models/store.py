
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores' #for mapping objects to the DB, we first define a table, define its columns. only the object values that match the columns will be mapped in DB

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))

    items= db.relationship('ItemModel', lazy='dynamic')


    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'items': [item.json() for item  in self.items.all()]}


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
