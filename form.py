# 2 videos I used for creating the form and pulling data from it
# https://www.youtube.com/watch?v=-O9NMdvWmE8
# https://www.youtube.com/watch?v=f8qvLBvrIFI

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ComputeForm(FlaskForm):
    distance = StringField('Distance')
    time = StringField('Time')
    pace = StringField('Pace')
    submit = SubmitField('submit')
