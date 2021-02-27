from marshmallow import fields, Schema 
import datetime

## imported from __init__.py
from . import db 
from . import bcrypt 

class UserModal(db.Model): 
    '''
    User Model
    '''

    ## Table name 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    ## util methods
    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
    def validate_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    ## class constructor
    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(value)
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @static_method
    def get_one_user(id):
        return UserModel.query.get(id)
    
    @static_method
    def get_all_users():
        return UserModel.query.all()

    def __repr(self):
        return '<id {}>'.format(self.id)




'''
    ## pointers

    - We imported db instance from __init__.py
    - Our Model class inherited from the db.Model 
'''
