from my_profile import app, db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    feedback = db.Column(db.String(500))

    def __init__(self, email, feedback):
        self.email = email
        self.feedback = feedback

    def __repr__(self):
        return f"The email is {self.email} and feedback is {self.feedback}"