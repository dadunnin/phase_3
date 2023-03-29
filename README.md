# phase_3

pip install Flask
pip install Flask-WTF
pip install email_validator
pip install Flask-SQLAlchemy Flask-Migrate

#if you change a model or something just run
flask db migrate -m "Add gender to Member model"
flask db upgrade