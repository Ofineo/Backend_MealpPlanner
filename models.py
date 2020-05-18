import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
#database_path = "postgres://postgres:postgres@localhost:5432/meals"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Table Ingredients
'''


class Ingredients(db.Model):
    __tablename__: 'Ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    quantity = Column(String(), nullable=False)

    '''
    insert()
    inserts a new model into a database
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
    updates a model into a database
    the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
    deletes a model into a database
    the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
        }
