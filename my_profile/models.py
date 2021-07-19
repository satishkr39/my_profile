from my_profile import app, db
from my_profile import login_manger
from flask_login import UserMixin


@login_manger.user_loader
def load_user(user_id):
    return  Admin.query.get(user_id)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    designation = db.Column(db.String(20))
    feedback = db.Column(db.String(500))

    def __init__(self, email, name, designation, feedback):
        self.email = email
        self.feedback = feedback
        self.name = name
        self.designation = designation

    def __repr__(self):
        return f"The email is {self.email} , name is {self.name}, designation is {self.designation} " \
               f"feedback is {self.feedback}"

class Admin(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(30))

    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def __repr__(self):
        return f" The username is {self.email_id}"

    def get_id(self):
        return (self.user_id)
