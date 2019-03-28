from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed


class AddNewCategoryForm(FlaskForm):
    category_name = StringField(validators=[DataRequired(), Length(min=2, max=50)])
    image_file = FileField('Add Photo', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add')
