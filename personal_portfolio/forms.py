from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    """Contact form for the contact page"""
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=50, message='Name must be between 2 and 50 characters')
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address')
    ])
    subject = StringField('Subject', validators=[
        DataRequired(),
        Length(min=3, max=100, message='Subject must be between 3 and 100 characters')
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=1000, message='Message must be between 10 and 1000 characters')
    ])
    submit = SubmitField('Send Message')
