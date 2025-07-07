from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class HealthForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired()])
    weight = IntegerField("Weight (kg)", validators=[DataRequired()])
    height = IntegerField("Height (cm)", validators=[DataRequired()])
    goal = SelectField("Goal", choices=[('lose', 'Weight Loss'), ('gain', 'Weight Gain'), ('maintain', 'Maintain')])
    restriction = StringField("Dietary Restrictions (comma separated)")
    submit = SubmitField("Generate Plan")
