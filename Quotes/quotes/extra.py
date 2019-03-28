# if request.method == "POST":
#     cat = request.form.get('select_value')
# else:
#     cat = None
#
# form = NewQuoteForm()
# categories = Categories.query.all()
# for one_cat in categories:
#     if cat is not None:
#         if one_cat.category_name in cat:
#             cat_id = one_cat.category_name
