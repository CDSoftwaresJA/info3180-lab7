from flask_wtf import FlaskForm
from wtforms import FileField,StringField


class UploadForm(FlaskForm):
    photo = FileField('image')
    description = StringField('Description')
   