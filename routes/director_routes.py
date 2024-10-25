from flask import render_template, redirect, url_for, Blueprint
from app import db
from models.director_model import Director
from services.session_scope import session_scope
from forms.director_form import DirectorForm
from flask_login import login_required

director_bp = Blueprint('directors', __name__)

@director_bp.route('/directors', methods=['GET'])
def list_directors():
    with session_scope() as session:
        directors = session.query(Director).all()
    return render_template('list_directors.html', directors=directors)

@director_bp.route('/directors/add', methods=['GET', 'POST'])
@login_required
def add_director():
    form = DirectorForm()
    if form.validate_on_submit():
        new_director = Director(name=form.name.data)
        with session_scope() as session:
            session.add(new_director)
        return redirect(url_for('directors.list_directors'))
    return render_template('add_director.html', form=form)


    
