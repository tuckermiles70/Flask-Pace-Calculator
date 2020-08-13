# https://www.youtube.com/watch?v=-O9NMdvWmE8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ComputeForm(FlaskForm):
    distance = StringField('Distance')
    time = StringField('Time')
    pace = StringField('Pace')
    submit = SubmitField('submit')
