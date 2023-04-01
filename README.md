# phase_3

# to activate the virtual environment
source venv/bin/activate

pip install Flask
pip install Flask-WTF
pip install email_validator
pip install Flask-SQLAlchemy Flask-Migrate

#if you change a model or something just run
flask db migrate -m "message goes here"
flask db upgrade