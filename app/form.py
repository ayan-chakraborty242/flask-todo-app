# create WTf
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class TodoApp(FlaskForm):
    task=StringField("Enter your Task",validators=[DataRequired(message="please your enter job")])
    submit=SubmitField("Add Task")