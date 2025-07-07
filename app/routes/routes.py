from flask import Blueprint, render_template, request
from app.forms.health_form import HealthForm
from app.utils.nutrition import generate_plan

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = HealthForm()
    plan = None
    if form.validate_on_submit():
        user_data = {
            'age': form.age.data,
            'weight': form.weight.data,
            'height': form.height.data,
            'goal': form.goal.data,
            'restrictions': form.restriction.data.split(',')
        }
        plan = generate_plan(user_data)
    return render_template('meal_plan.html', form=form, plan=plan)
