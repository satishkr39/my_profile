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
        from_email = os.getenv('email')
        to_email = os.getenv('to_email')
        keyvalue = os.getenv('test_key')
        name = form.name.data
        user_email = form.email.data
        designation = form.designation.data
        feedback = form.feedback.data
        form.send_mail(user_email=user_email, feedback=feedback, designation=designation, keyvalue=keyvalue,
                       from_email=from_email, to_email=to_email, name=name)
        user = Users(email=user_email, name=name, designation=designation, feedback= feedback)
        db.session.add(user)
        db.session.commit()
        flash("Thank you for your feedback.")
        # return redirect(url_for('index'))
    return render_template('contact.html', form=form)