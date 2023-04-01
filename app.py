from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_secret_key"

# This guy creates our database in app.db within our project
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Spin up the db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/success')
def success():
    return 'It worked!'

# Import and register the blueprint after initializing the db
from routes.member_routes import member_blueprint
app.register_blueprint(member_blueprint, url_prefix="/member")

if __name__ == '__main__':
    app.run()
