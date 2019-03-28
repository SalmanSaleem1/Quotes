from flask import Blueprint, render_template, request, url_for

from quotes.models import Quotes

main = Blueprint('main', __name__)


@main.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    quote = Quotes.query.order_by(Quotes.created_at.desc(), Quotes.updated_at.asc()).paginate(page=page, per_page=8)
    image_file = url_for('static', filename='images/')
    return render_template('homw2.html', quote=quote, title='Home', image_file=image_file)
