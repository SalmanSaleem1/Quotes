from quotes import db
from datetime import datetime


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80))

    def __repr__(self):
        return f"Categories('{self.category_name}', '{self.id}')"


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
    category_id = db.Column(db.String(100), db.ForeignKey('categories.category_name'))

    def __repr__(self):
        return f"Quotes('{self.quote}', '{self.category_id}')"

