from app.ai.coach import generate_motivation_for_habit

# Sample habits to test
habits = ["drink more water", "meditate", "walk after dinner"]

# Loop through each habit and print the AI message
for habit in habits:
    message = generate_motivation_for_habit(habit)
    print(f"Habit: {habit}\nMotivation: {message}\n{'-'*40}")
