from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[
                             DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[
                            DataRequired(), Length(min=2, max=50)])
    age = IntegerField('Age', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[
                           DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', format='%Y-%m-%d',
                    validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=30)])
    submit = SubmitField('Create User')
