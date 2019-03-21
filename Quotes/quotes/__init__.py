from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.secret_key = '1234657889'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy(app)


from quotes.categories.routes import category
from quotes.quote.routes import quote
from quotes.main.routes import main
from quotes.errors.routes import error

app.register_blueprint(category)
app.register_blueprint(quote)
app.register_blueprint(main)
app.register_blueprint(error)




