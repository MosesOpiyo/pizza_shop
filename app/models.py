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

    def __repr__(self):
        return f'User {self.username}'