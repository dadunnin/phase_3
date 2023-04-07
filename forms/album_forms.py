from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length


class CreateAlbumForm(FlaskForm):
    album_name = StringField('Album Name', validators=[DataRequired(), Length(min=1, max=50)] )
    submit = SubmitField('Create')
