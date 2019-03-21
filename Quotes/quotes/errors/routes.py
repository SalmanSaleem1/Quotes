from flask import Blueprint, render_template

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@error.app_errorhandler(403)
def error_403():
    return ''
