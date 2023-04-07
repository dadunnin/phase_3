from flask import Blueprint, render_template, redirect, url_for
from datetime import datetime
from forms.album_forms import CreateAlbumForm
from flask_login import current_user

album_blueprint = Blueprint('album_blueprint', __name__)

@album_blueprint.route('/test-insert', methods=['GET', 'POST'])
def testInsert():
    from models.Member import Member
    from models.Album import Album
    from app import db
    member = Member.query.get(1)
    album = Album(name="Test Album", owner_id=member.id, created=datetime.utcnow()) # Pass the member object instead of member.id

    db.session.add(album)
    db.session.commit()
    return "album created successfully"

@album_blueprint.route('/test-delete', methods=['GET', 'POST'])
def testDelete():
    from models.Member import Member
    from models.Album import Album
    from app import db
    album = Album.query.filter_by(name="Test Album").first()

    if not album:
        return "could not get album"

    db.session.delete(album)
    db.session.commit()

    return 'album was deleted'

@album_blueprint.route('/create', methods=['GET', 'POST'])
def createAlbum():
    from models.Album import Album
    from app import db

    # Check if the user is logged in
    if not current_user.is_authenticated:
        return redirect(url_for('member_blueprint.signin'))

    form = CreateAlbumForm()
    if form.validate_on_submit():
        album = Album(
            name = form.album_name.data,
            created = datetime.utcnow(),
            owner_id=current_user.id
        )
        db.session.add(album)
        db.session.commit()
        return redirect(url_for('success'))

    return render_template('create_album.html', title='Create Album', form=form)

