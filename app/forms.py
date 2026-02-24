from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name(Required)', validators=[DataRequired()])
    email = StringField('Email(Required)', validators=[DataRequired(), Email()])
    subject = StringField('Subject(Required)', validators=[DataRequired()])
    message = StringField('Message(Required)', validators=[DataRequired()])
    submit = SubmitField('Send')