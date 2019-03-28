from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators
from flask_wtf.file import FileAllowed, FileField


class NewQuoteForm(FlaskForm):
    quote = StringField('Quote', [validators.required()])
    language = StringField('Language', [validators.required()])
    color_code = StringField('Color Code', [validators.required()])
    font_family = StringField('Font Family')
    image_file = FileField('Add Photo', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add')
