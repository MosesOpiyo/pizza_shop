from . import db

class User(db.Model):
    """This will define all behaviours of the user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    location = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class Roles(db.Model):
    """This defines the users roles

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

class Pizza(db.Model):
    """This defines the behaviours of an individual pizza

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'pizza'
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255))
    base_price = db.Column(db.Integer)