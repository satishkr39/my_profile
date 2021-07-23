from flask import render_template, flash, redirect, url_for, Blueprint, request
from flask_login import login_user, logout_user,current_user, login_required
from my_profile.users.forms import LoginForm
from my_profile.models import Admin, Users

user_blueprint = Blueprint('user', __name__, template_folder='templates/users')

# login method
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email_id=form.username.data).first()
        if  user is not None and user.check_password(form.password.data):
            login_user(user)  # in-built function for flask_login_manager.
            # flash("you are login now")
            all_data = Users.query.all()  # get all the data
            return render_template('view_data.html', data=all_data)
        else:
            flash("Invalid Username or Password")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

# logout user
@login_required
@user_blueprint.route('/logout')
def logout():
    logout_user()
    flash("You are logged out now")
    return redirect(url_for('index'))