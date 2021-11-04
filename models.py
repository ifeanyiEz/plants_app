from os import name
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, defaultload


#________________Configure the application______________________________#


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db = SQLAlchemy(app)
Migrate(app, db)
#CORS(app, resources={r"*/api/*" : {origins: '*'}})
CORS(app)



#________________Define the models__________________________________#

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=True)
    scientific_name = db.Column(db.String(120), nullable=True)
    is_poisonous = db.Column(db.Boolean, nullable=False, default=False)
    primary_color = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return 'Plant: {} {} {} {}'.format(self.name, self.scientific_name, self.is_poisonous, self.primary_color)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'is_poisonous': self.is_poisonous,
            'primary_color': self.primary_color
        }
