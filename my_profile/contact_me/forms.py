from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import smtplib

class AboutForm(FlaskForm):
    name = StringField("Enter your name ", validators=[DataRequired()])
    email = StringField("Enter your mail id", validators=[DataRequired(), Email()])
    designation = StringField("Enter your deignation/role ", validators=[DataRequired()])
    feedback = TextAreaField("Enter any valuable feedback or query", validators=[DataRequired()])
    submit = SubmitField("Submit")


    def send_mail(self, user_email, feedback, designation, keyvalue, from_email, to_email, name):
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("satishsinghkumarr@gmail.com", keyvalue)

        # message to be sent
        text = "Name: "+name +"\n Sender Mail ID: " + user_email+"\n Designation: "+ designation+"\n Feedback: "+feedback
        subject = "Mail from your website"
        message = 'Subject: {}\n\n{}'.format(subject, text)
        # sending the mail
        s.sendmail(from_email, to_email, message)

        # terminating the session
        s.quit()