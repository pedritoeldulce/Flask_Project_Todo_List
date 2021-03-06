from . import db
import datetime

from werkzeug.security import  generate_password_hash


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # password = db.Column(db.String(93), nullable=False)
    encrypted_password = db.Column(db.String(93), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.encrypted_password = generate_password_hash(value)
    
    def __str__(self):
        return self.username

    @classmethod
    def create_element(cls, username, password, email):
        user = Users(username=username, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return user