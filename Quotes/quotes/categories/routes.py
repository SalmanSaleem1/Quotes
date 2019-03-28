from flask import Blueprint, render_template, request, abort, flash, redirect, url_for
from quotes.models import Categories, Quotes
from quotes.categories.forms import AddNewCategoryForm
from quotes import db
from quotes.categories.utils import savePicture
import facebook

category = Blueprint('category', __name__)


@category.route('/categories', methods=['GET', 'POST'])
def get_categories():
    # api_key = request.headers.get(ApiKeys.REQUEST_KEY_API_KEY)
    # if api_key is None:
    #     abort(403, AppConstant.MESSAGE_UNAUTHORIZED)
    #
    # if api_key != AppConstant.API_KEY:
    #     abort(403, AppConstant.MESSAGE_UNAUTHORIZED)
    categories = Categories.query.all()
    quote = Quotes.query.all()
    # categories_list = []
    # for u in categories:
    #     categories_list.append(object_as_dict(u))
    # return jsonify(categories_list)
    return render_template('categories.html', categories=categories, title='Add Categories', quote=quote)


@category.route('/add_new_category', methods=['POST', 'GET'])
def add_new_category():
    categories = Categories.query.all()
    form = AddNewCategoryForm()
    if form.validate_on_submit():
        if form.image_file.data:
            image_fil = savePicture(form.image_file.data)
        cat = Categories(category_name=form.category_name.data, image_file=image_fil)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('category.get_categories'))
    return render_template('add_new_category.html', form=form, label='Add New Category', categories=categories)


@category.route('/detail_category<string:category_id>', methods=['POST', 'GET'])
def get_categoryDetail(category_id):
    quote = Quotes.query.filter_by(category_id=category_id).all()
    return render_template('categoryDetail.html', title='Detail', quote=quote)


@category.route('/showCatgegories')
def showCat():
    categories = Categories.query.all()
    return render_template('categoriesWithPics.html', categories=categories)
