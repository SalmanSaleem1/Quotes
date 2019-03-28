from quotes import db, bcrypt, login
from datetime import datetime
from flask_login import UserMixin


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(60), default='default.jpg')
    category_name = db.Column(db.String(80))

    def __repr__(self):
        return f"Categories('{self.category_name}', '{self.id}', '{self.image_file}')"


class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(100))
    quote_by = db.Column(db.String(100), default='')
    language = db.Column(db.String(100), default='en')
    color_code = db.Column(db.String(100), default='#ffffff')
    font_family = db.Column(db.String(100), default='default')
    is_active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow())
    image_file = db.Column(db.String(60), default='default.jpg')
    category_id = db.Column(db.String(100), db.ForeignKey('categories.category_name'))

    def __repr__(self):
        return f"Quotes('{self.quote}', '{self.category_id}', '{self.image_file}')"


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return f"User('{self.name}', '{self.username}', '{self.email}', ('{self.password}'))"
