from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, TextField
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.required(DataRequired), validators.Email()])
    password = PasswordField('Password', [validators.required(DataRequired)])
    submit = SubmitField('Login')
