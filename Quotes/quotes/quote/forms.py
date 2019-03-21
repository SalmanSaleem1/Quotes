from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class NewQuoteForm(FlaskForm):
    category_id = StringField()
    quote = TextAreaField()
    # quote_by = StringField()
    language = StringField()
    color_code = StringField('Color Code')
    font_family = StringField()
    submit = SubmitField('Save')
