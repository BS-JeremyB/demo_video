from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from models.user_model import User
from forms.register_form import RegistrationForm
from forms.login_form import LoginForm
from flask_login import login_user, logout_user


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('movies.list_movies'))
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('movies.list_movies'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('auth.login'))