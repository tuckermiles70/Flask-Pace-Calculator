# https://www.youtube.com/watch?v=-O9NMdvWmE8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SignUpForm(FlaskForm):
    distance = StringField('Distance')
    time = StringField('time')
    pace = StringField('pace')
    submit - SubmitField('Submit')
