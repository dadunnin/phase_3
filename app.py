from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_secret_key"

# This guy creates our database in app.db within our project
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure photo uploads
photos = UploadSet('photos', IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "images"
configure_uploads(app, photos)

# Spin up the db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up flask login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from models.Member import Member
    return Member.query.get(int(user_id))

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/success')
def success():
    return 'It worked!'

# Import and register the blueprint after initializing the db
from routes.member_routes import member_blueprint
app.register_blueprint(member_blueprint, url_prefix="/member")

from routes.album_routes import album_blueprint
app.register_blueprint(album_blueprint, url_prefix="/album")

from routes.photo_routes import photo_blueprint
app.register_blueprint(photo_blueprint, url_prefix="/photo")

if __name__ == '__main__':
    app.run()
