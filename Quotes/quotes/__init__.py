from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from quotes.config import Config

# app = Flask(__name__, template_folder='template')
# app.secret_key = '1234657889'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = 'user.login'
login.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__, template_folder='template')
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    from quotes.categories.routes import category
    from quotes.quote.routes import quote
    from quotes.main.routes import main
    from quotes.errors.routes import error
    from quotes.user.routes import user

    app.register_blueprint(category)
    app.register_blueprint(quote)
    app.register_blueprint(main)
    app.register_blueprint(error)
    app.register_blueprint(user)

    return app
