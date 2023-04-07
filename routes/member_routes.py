from curses import flash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user
from forms.member_forms import LoginForm, RegistrationForm

member_blueprint = Blueprint('member_blueprint', __name__)

@member_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    from models.Member import Member
    from app import db
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
        return redirect(url_for('member_blueprint.signin'))
        
    return render_template('register.html', form=form)

@member_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    from models.Member import Member
    form = LoginForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(email=form.email.data).first()
        if member is None or not member.check_password(form.password.data):
            return redirect(url_for('member_blueprint.signin'))
        login_user(member, remember=False)
        return redirect(url_for('success'))
    return render_template('login.html', title='Sign In', form=form)