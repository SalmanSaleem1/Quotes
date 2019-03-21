from flask import Blueprint, render_template, redirect, url_for, flash, request
from quotes.quote.forms import NewQuoteForm
from quotes.models import Quotes, Categories
from quotes import db

quote = Blueprint('quote', __name__)


@quote.route('/add_quote', methods=['POST', 'GET'])
def add_new_quote():
    if request.method == "POST":
        cat = request.form.get('select_value')
    else:
        cat = None
    form = NewQuoteForm()
    categories = Categories.query.all()
    #
    # cat_id = []
    for one_cat in categories:
        if cat == one_cat.category_name:
            cat_id = one_cat.category_name
            break
    # print(cat_id)
    if form.validate_on_submit():
        print("come here")
        que = Quotes(category_id=cat_id, quote=form.quote.data, language=form.language.data
                     , color_code=form.color_code.data, font_family=form.font_family.data)
        db.session.add(que)
        db.session.commit()
        flash(f'Save Successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_new_quote.html', title='Add New Quotes', legend='Add new Quote',
                           form=form, categories=categories)


@quote.route('/<int:quote_id>', methods=['POST', 'GET'])
def get_byID(quote_id):
    que = Quotes.query.get_or_404(quote_id)
    return render_template('quoteDetail.html', title='', que=que)


@quote.route('/delete/<int:quote_id>', methods=['POST', 'GET'])
def delete_byID(quote_id):
    que = Quotes.query.get_or_404(quote_id)
    db.session.delete(que)
    db.session.commit()
    flash(f'Delete Successfully', 'success')
    return redirect(url_for('main.home'))


@quote.route('/update/<int:quote_id>', methods=['POST', 'GET'])
def update_byID(quote_id):
    if request.method == "POST":
        cat = request.form.get('select_value')
    else:
        cat = None
    form = NewQuoteForm()
    categories = Categories.query.all()
    for one_cat in categories:
        if cat == one_cat.category_name:
            cat_id = one_cat.category_name
            break
    # print(cat_id)
    que = Quotes.query.get_or_404(quote_id)
    if form.validate_on_submit():
        que.category_id = cat_id
        que.quote = form.quote.data
        que.language = form.language.data
        que.color_code = form.color_code.data
        que.font_family = form.font_family.data
        db.session.commit()
        return redirect(url_for('main.home', quote_id=que.id))
    elif request.method == 'GET':

        form.quote.data = que.quote
        form.language.data = que.language
        form.color_code.data = que.color_code
        form.font_family.data = que.font_family
        flash(f'Delete Successfully', 'success')
    return render_template('add_new_quote.html', title='Update Quote', form=form, que=que, legend='Update Quotation', categories=categories)

