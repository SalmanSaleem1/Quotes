from flask import Blueprint, render_template, request, abort, flash, redirect, url_for
from sqlalchemy import inspect
from quotes.models import Categories, Quotes
from flask import jsonify


from quotes.categories.forms import CategoriesForm, AddNewCategoryForm
from quotes import db

category = Blueprint('category', __name__)


@category.route('/categories', methods=['GET', 'POST'])
def get_categories():
    # api_key = request.headers.get(ApiKeys.REQUEST_KEY_API_KEY)
    # if api_key is None:
    #     abort(403, AppConstant.MESSAGE_UNAUTHORIZED)
    #
    # if api_key != AppConstant.API_KEY:
    #     abort(403, AppConstant.MESSAGE_UNAUTHORIZED)
    form = CategoriesForm()
    categories = Categories.query.all()
    # categories_list = []
    # for u in categories:
    #     categories_list.append(object_as_dict(u))
    # return jsonify(categories_list)
    return render_template('categories.html', form=form, categories=categories, title='Add Categories')


@category.route('/add_new_category', methods=['POST', 'GET'])
def add_new_category():
    form = AddNewCategoryForm()
    if form.validate_on_submit():
        cat = Categories(category_name=form.category_name.data)
        db.session.add(cat)
        db.session.commit()

        return redirect(url_for('category.get_categories'))
    return render_template('add_new_category.html', form=form)


@category.route('/detail_category<string:category_id>', methods=['POST', 'GET'])
def get_categoryDetail(category_id):
    quote = Quotes.query.filter_by(category_id=category_id).all()
    return render_template('categoryDetail.html', title='', quote=quote)


