from flask import Blueprint, render_template, request, redirect, url_for
from quotes.user.forms import LoginForm
from quotes.models import User
from quotes import bcrypt
from flask_login import login_user, current_user


user = Blueprint('user', __name__)


@user.route('/login', methods=['POST', 'GET'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        print('come here')
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.home'))
    return render_template('login.html', form=form, title='Login')
