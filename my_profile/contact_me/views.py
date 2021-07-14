from flask import render_template, Blueprint, url_for

contact_blueprint = Blueprint('contact', __name__, template_folder='templates/contact_me')

@contact_blueprint.route('/contact')
def contact_method():
    return render_template('contact.html')