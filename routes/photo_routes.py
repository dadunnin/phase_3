from flask import Blueprint, render_template, redirect, url_for
from datetime import datetime
from forms.album_forms import CreateAlbumForm
from flask_login import current_user

from forms.photo_forms import UploadPhotoForm

photo_blueprint = Blueprint('photo_blueprint', __name__)

@photo_blueprint.route('/upload', methods=['GET', 'POST'])
def upload_photo():
    from models.Album import Album
    from models.Photo import Photo
    from app import db
    from app import photos

    form = UploadPhotoForm()
    form.album.choices = [(a.id, a.name) for a in Album.query.all()]

    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        photo = Photo(album_id=form.album.data, caption=form.caption.data, img=filename)
        db.session.add(photo)
        db.session.commit()
        return redirect(url_for('success'))

    return render_template('upload_photo.html', form=form)