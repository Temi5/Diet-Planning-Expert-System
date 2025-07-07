import pandas as pd
import random

def generate_plan(user_data):
    df = pd.read_csv("data/nutrition.csv")

    # Preprocess: lowercase column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove rows with missing calorie values
    df = df[df['calories'].notnull()]

    # Filter out restricted foods
    restrictions = [r.strip().lower() for r in user_data.get("restrictions", []) if r.strip()]
    if restrictions:
        df = df[~df['name'].str.lower().str.contains('|'.join(restrictions))]

    # Goal-based daily calorie target
    goal = user_data.get("goal", "maintain")
    weight = user_data.get("weight", 70)

    calorie_targets = {
        "lose": weight * 25,       # ~25 kcal/kg for weight loss
        "maintain": weight * 30,   # ~30 kcal/kg to maintain
        "gain": weight * 35        # ~35 kcal/kg for weight gain
    }
    target_calories = calorie_targets.get(goal, 2100)

    # Randomly assemble meals to match calorie target
    meals = {"Breakfast": [], "Lunch": [], "Dinner": []}
    remaining_calories = target_calories
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle

    for _, row in df.iterrows():
        if remaining_calories <= 0:
            break
        item = {
            "name": row["name"],
            "calories": row["calories"]
        }
        # Assign to a meal based on total left
        if remaining_calories > 0.6 * target_calories:
            meals["Breakfast"].append(item)
        elif remaining_calories > 0.3 * target_calories:
            meals["Lunch"].append(item)
        else:
            meals["Dinner"].append(item)
        remaining_calories -= row["calories"]

    # Format meal data
    formatted_meals = []
    for meal, items in meals.items():
        formatted_meals.append({
            "meal": meal,
            "items": [i["name"] for i in items],
            "calories": round(sum(i["calories"] for i in items), 2)
        })

    return formatted_meals
