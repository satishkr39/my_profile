from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    email = StringField("Enter your mail id", validators=[DataRequired(), Email()])
    feedback = TextAreaField("Enter any valuable feedback or questions", validators=[DataRequired()])
    submit = SubmitField("Submit")