from my_profile import app
from flask import Blueprint, render_template

certificate_blueprint = Blueprint('certificate',__name__, template_folder='templates/certificate')


@certificate_blueprint.route('/certificate')
def certificate():
    return render_template('certificate.html')