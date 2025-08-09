from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 🔄 Reverse Diet Generator
def get_reverse_diet(goal):
    goal = goal.lower()
    if "lose weight" in goal:
        return "Eat 5 scoops of ice cream before bed. 🍦"
    elif "build muscle" in goal:
        return "Avoid protein. Only eat marshmallows. 💪➡️🍬"
    elif "fit" in goal:
        return "Sit still. Hydrate with soda. 🛋️🥤"
    elif "healthy" in goal or "health" in goal:
        return "Deep-fry everything. Even your salad. 🥗🔥"
    else:
        return "Eat unpredictably. Trust your cravings. 🧠🍕"

# 📉 Reverse Progress Tracker
def get_progress_message(current_weight, previous_weight):
    try:
        current = float(current_weight)
        previous = float(previous_weight)
        if current > previous:
            return "Amazing! You’re defying gravity. 🎈"
        elif current < previous:
            return "Oh no! You’re ruining the ReverseFit legacy. 😢"
        else:
            return "Perfect. Stagnation is the key to greatness. 🧘‍♂️"
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    tips = [
        "Do 10 squats every time you say 'bro'.",
        "Replace dumbbells with watermelons. More fun.",
        "Running late counts as cardio.",
        "Stretch your excuses before your muscles."
    ]
    random_tip = random.choice(tips)
    user_goal = None
    reverse_diet = None
    progress_message = None
    user_name = None

    if request.method == 'POST':
        user_name = request.form.get('name')
        user_goal = request.form.get('goal')
        reverse_diet = get_reverse_diet(user_goal)

        current_weight = request.form.get('current_weight')
        previous_weight = request.form.get('previous_weight')
        progress_message = get_progress_message(current_weight, previous_weight)

    return render_template('index.html', tip=random_tip, name=user_name, goal=user_goal, diet=reverse_diet, progress=progress_message)

if __name__ == '__main__':
    app.run(debug=True)
