import os.path
from flask import Flask, flash
from flask import render_template, url_for, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manger = LoginManager()
login_manger.init_app(app)
login_manger.login_view = 'login_user'  # need to check

db = SQLAlchemy(app)
Migrate(app, db)


@app.route('/')
def index():
    start_date = datetime(2019, 6, 12, 12, 33)
    end_date = datetime.today()
    diffyears = end_date.year - start_date.year
    return render_template('home.html', year=diffyears)


from my_profile.certificate.views import certificate_blueprint
from my_profile.skills.views import skills_blueprint
from my_profile.academics.views import academics_blueprint
from my_profile.contact_me.views import contact_blueprint
from my_profile.users.views import user_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(certificate_blueprint)
app.register_blueprint(skills_blueprint)
app.register_blueprint(academics_blueprint)
app.register_blueprint(contact_blueprint)