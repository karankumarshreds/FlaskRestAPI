from marshmallow import fields, Schema 
import datetime

## imported from __init__.py
from . import db 
from . import bcrypt 

class BlogModel(db.Model):
    '''
    BlogModel
    '''
    
    ## Table name 
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.owner_id = data.get('owner_id')
        
    def save(self):
        db.session.add(self)
        db.session.commit(self)
    
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def get_all_blogposts():
        return BlogpostModel.query.all()

    @staticmethod
    def get_one_blogpost(id):
        return BlogpostModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)
        
        
class BlogSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    contents = fields.Str(required=True)
    owner_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)