from flask import render_template, Blueprint, url_for

academics_blueprint = Blueprint('academics', __name__, template_folder='templates/academics')

@academics_blueprint.route('/academics')
def academics_method():
    return render_template('academics.html')