from flask_wtf import FlaskForm 
from wtforms import TextField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm): 
    name=TextField('Name', validators=[DataRequired()]) 
    email=TextField('E-mail', validators=[DataRequired(), Email()]) 
    subject=TextField('Subject',validators=[DataRequired()])
    message=TextAreaField('Message',validators=[DataRequired()])
    