from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class SomeForm(FlaskForm):
    input1 = StringField("Input 1", validators=[DataRequired()])
    input2 = StringField("Input 2", validators=[DataRequired()])
    submit = SubmitField("Submit")
