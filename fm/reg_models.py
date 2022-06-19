from email import message
from operator import le
from random import choices
from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, SelectMultipleField

class regLaserForm(FlaskForm):
    laser_mechine = SelectMultipleField(
        label='chi',
        choices = (
            (1, 'TRP'),
            (2, 'NTC'),
        )
    )

    laser_project = StringField(
        label='laser_project',
        validators=[DataRequired(), Length(2,30)]
    )

    laser_partNo = StringField(
        label='laser_partNo',
        validators=[DataRequired(), Length(2, 20)]
    )

    laser_worker = StringField(
        label='laser_worker',
        validators=[DataRequired()]
    )
    
    laser_qty = StringField(
        label = 'laser_qty',
        validators=[DataRequired()]
    )

    laser_defective = StringField(
        label = 'defective',
        validators=[DataRequired()]
    )
    laser_submit = SubmitField(
        label='regLaser'
    )
