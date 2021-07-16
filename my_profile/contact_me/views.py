from flask import render_template, Blueprint, url_for, flash, redirect
from my_profile.contact_me.forms import AboutForm
from my_profile.models import Users
from my_profile import db
import time
import os

contact_blueprint = Blueprint('contact', __name__, template_folder='templates/contact_me')

@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact_method():
    form = AboutForm()
    # global keyvalue
    keyvalue = os.getenv('test_key')
    if form.validate_on_submit():
        keyvalue = os.getenv('test_key')
        user_email = form.email.data
        feedback = form.feedback.data
        print(user_email, feedback)
        user = Users(user_email, feedback)
        print("User entered the following Data: ", user)
        #db.session.add(user)
        #db.session.commit()
        flash("Thank you for your feedback.")
        print(keyvalue)
        # return redirect(url_for('index'))
    return render_template('contact.html', form=form, keyvalue=keyvalue)