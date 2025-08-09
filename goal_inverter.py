def reversefit_goal(goal_text):
    words = goal_text.lower().split()
    weight = None
    time = None
    intent = None
    weight_unit = None
    time_unit = None

    for i, word in enumerate(words):
        if word == "lose":
            intent = "lose"
        elif word == "gain":
            intent = "gain"
        if word.replace('.', '', 1).isdigit():
            if i + 1 < len(words):
                next_word = words[i + 1]
                if "kg" in next_word or "lbs" in next_word:
                    weight = float(word)
                    weight_unit = next_word
                elif any(unit in next_word for unit in ["day", "days", "week", "weeks", "month", "months", "year", "years"]):
                    time = int(word)
                    time_unit = next_word

    if not intent or weight is None or time is None:
        raise ValueError("Invalid goal format. Please include intent (lose/gain), weight, and time.")

    # Convert lbs to kg
    if weight_unit == "lbs":
        weight = round(weight * 0.45, 1)

    # Convert time to weeks
    if time_unit in ["days", "day"]:
        time = max(1, time // 7)
    elif time_unit in ["weeks", "week"]:
        time = time
    elif time_unit in ["months", "month"]:
        time = time * 4
    elif time_unit in ["years", "year"]:
        time = time * 52
    else:
        raise ValueError("Unsupported time unit. Use days, weeks, months, or years.")

    inverted_intent = "gain" if intent == "lose" else "lose"
    inverted_time = max(1, time // 2)
    inverted_weight = round(weight, 1)

    inverted_goal = f"{inverted_intent.capitalize()} {inverted_weight} kg in {inverted_time} weeks"

    messages = [
        f"🔥 New Goal: {inverted_goal}! Let’s bulk up with style!",
        f"🎉 Forget salads—embrace the snack life. {inverted_goal} is your destiny!",
        f"💪 You’re not just gaining weight, you’re gaining *character*. {inverted_goal} starts now!"
    ]

    return inverted_goal, messages
