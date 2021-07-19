from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm, UserMixin):
    username = StringField("Enter your username: ", validators=[DataRequired()])
    password = PasswordField("Enter your password: ", validators=[DataRequired()])
    submit = SubmitField("Login")
