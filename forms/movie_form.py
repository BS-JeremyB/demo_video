from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from models.director_model import Director

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    director_id = SelectField('Director', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Movie')

    def populate_director_choices(self):
        self.director_id.choices = [(director.id, director.name) for director in Director.query.all()]