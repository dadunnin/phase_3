from flask import Blueprint, render_template, redirect, url_for
from app import app, db
from forms import RegistrationForm
from models.Member import Member

member_blueprint = Blueprint('member_blueprint', __name__)

@member_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        member = Member(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            dob=form.dob.data,
            hometown=form.hometown.data,
            gender=form.gender.data
        )
        member.set_password(form.password.data)

        db.session.add(member)
        db.session.commit()
        return redirect(url_for('success'))
        
    return render_template('register.html', form=form)