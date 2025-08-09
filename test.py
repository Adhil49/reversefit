# test.py

from goal_inverter import reversefit_goal

user_input = "I want to lose 5 kg in 2 months"
inverted_goal, funny_messages = reversefit_goal(user_input)

print("🚫 Original Goal:", user_input)
print("✅ Inverted Goal:", inverted_goal)
print("💬 Motivational Messages:")
for msg in funny_messages:
    print("-", msg)
