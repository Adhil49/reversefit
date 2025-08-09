from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Funny sabotage tips
tips = [
    "Eat cake before cardio. Always.",
    "Replace water with soda for hydration.",
    "Sleep through your workout. It's restorative.",
    "Stretch your excuses, not your muscles.",
    "Reverse progress is still progress!"
]

@app.route("/", methods=["GET", "POST"])
def home():
    tip = random.choice(tips)
    name = goal = diet = progress = ""
    
    if request.method == "POST":
        name = request.form["name"]
        goal = request.form["goal"]
        current_weight = float(request.form["current_weight"])
        target_weight = float(request.form["target_weight"])

        # Reverse sabotage logic
        sabotage_weight = current_weight + (target_weight - current_weight) * 1.5
        progress = f"You gained {sabotage_weight - current_weight:.1f} kg instead of losing it!"
        diet = "Eat more carbs, skip protein, and nap aggressively."

    return render_template("index.html", tip=tip, name=name, goal=goal, diet=diet, progress=progress)

if __name__ == "__main__":
    app.run(debug=True)
