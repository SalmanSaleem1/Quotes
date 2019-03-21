from flask import Blueprint, render_template, url_for, request
from quotes.models import Quotes

main = Blueprint('main', __name__)


@main.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    quote = Quotes.query.order_by(Quotes.created_at.desc(), Quotes.updated_at.desc()).paginate(page=page, per_page=5)

    return render_template('home.html', quote=quote, title='Home')
