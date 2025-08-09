from flask import Flask, render_template, request
from goal_inverter import reversefit_goal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    messages = []
    error = None

    if request.method == "POST":
        user_goal = request.form.get("goal")
        try:
            inverted_goal, messages = reversefit_goal(user_goal)
            result = inverted_goal

            # Save to file
            with open("saved_goals.txt", "a", encoding="utf-8") as file:
                file.write("🎯 Original Goal: " + user_goal + "\n")
                file.write("🔄 Inverted Goal: " + inverted_goal + "\n")
                file.write("🤣 Funny Motivation:\n")
                for msg in messages:
                    file.write("- " + msg + "\n")
                file.write("\n")

        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, messages=messages, error=error)

@app.route("/history")
def history():
    try:
        with open("saved_goals.txt", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No saved goals yet."
    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
