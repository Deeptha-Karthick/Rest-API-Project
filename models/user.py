import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__= 'users' #for mapping objects to the DB, we first define a table, define its columns. only the object values that match the columns will be mapped in DB

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        
        self.username= username
        self.password= password

    #def find_by_username(self, username): #since we aren using self anywhere we can just cchange it to a class method
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username= username).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id= _id).first()

    def save_to_db(self): #inserts and updating the data
        db.session.add(self)
        db.session.commit()
