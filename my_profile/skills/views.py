from flask import Blueprint, render_template
import os
skills_blueprint = Blueprint('skills',__name__, template_folder='templates/skills')

@skills_blueprint.route('/skills')
def skills():
    return render_template('skills.html')