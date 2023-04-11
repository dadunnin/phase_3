from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UploadPhotoForm(FlaskForm):
    album = SelectField('Select Album', coerce=int, validators=[DataRequired()])
    caption = StringField('Caption')
    photo = FileField('Choose a photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])
    submit = SubmitField('Create')
