from flask import Flask
from flask import render_template, url_for, redirect
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

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

app.register_blueprint(certificate_blueprint)
app.register_blueprint(skills_blueprint)
app.register_blueprint(academics_blueprint)
app.register_blueprint(contact_blueprint)