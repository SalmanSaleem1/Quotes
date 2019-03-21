from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoriesForm(FlaskForm):
    category_name = StringField(validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Save')


class AddNewCategoryForm(FlaskForm):
    category_name = StringField(validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Add')
