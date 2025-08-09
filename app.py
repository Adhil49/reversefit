from flask import Flask, render_template, request
import time
import random

app = Flask(__name__)

# 🏋️ Fitness Tips
fitness_tips = [
    "Stretch your excuses before your muscles.",
    "Running late counts as cardio.",
    "Abs are made in the kitchen... and lost in the fridge.",
    "Drink water like it's a pre-workout potion.",
    "Rest days are sacred. Like Sundays and pizza.",
    "Sweat is just your fat crying. Loudly.",
    "If you can't pronounce it, don't eat it. Unless it's chocolate."
]

# 🍽️ Diet Plans
diet_plans = [
    "Eat only foods that start with the letter Q.",
    "Replace all meals with motivational quotes.",
    "One grape every hour. Stay strong.",
    "Keto, but with cake.",
    "Intermittent fasting: fast between snacks.",
    "Only eat what you can lift. Goodbye watermelon."
]

# 💬 Quotes
quotes = [
    "Success is stumbling from failure to failure with no loss of enthusiasm.",
    "You miss 100% of the naps you don’t take.",
    "Fitness is 90% mental. The other half is physical.",
    "Don’t count the reps. Make the reps count. Or just count sheep.",
    "Your only limit is your fridge."
]


@app.route("/", methods=["GET", "POST"])
def home():
    tip = random.choice(fitness_tips)
    if request.method == "POST":
        name = request.form["name"]
        goal = request.form["goal"].lower()
        current_weight = float(request.form["current_weight"])
        target_weight = float(request.form["target_weight"])

        time.sleep(5)  # Simulate loading

        sabotage_type = ""
        sabotage_amount = abs(target_weight - current_weight) * 1.5

        if "gain" in goal:
            sabotage_type = "lost"
            sabotage_weight = current_weight - sabotage_amount
        elif "lose" in goal:
            sabotage_type = "gained"
            sabotage_weight = current_weight + sabotage_amount
        else:
            sabotage_type = "fluctuated"
            sabotage_weight = current_weight + random.uniform(-5, 5)

        sabotage_weight = round(sabotage_weight, 1)
        sabotage_amount = round(abs(sabotage_weight - current_weight), 1)

        progress = f"You have {sabotage_type} {sabotage_amount} kg instead of reaching your goal."
        achieved = f"Achieved: {sabotage_weight} kg"
        diet = random.choice(diet_plans)
        quote = random.choice(quotes)

        return render_template(
            "index.html",
            tip=tip,
            name=name,
            goal=goal,
            achieved=achieved,
            progress=progress,
            diet=diet,
            quote=quote
        )

    return render_template("index.html", tip=tip)

if __name__ == "__main__":
    app.run(debug=True)
