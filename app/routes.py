from flask import Blueprint, render_template, request, redirect, url_for
from app.ai.coach import generate_motivation_for_habit
from app.utils.storage import load_habits, save_habits
from datetime import date, datetime, timedelta  # ✅ includes timedelta now

main = Blueprint('main', __name__)

def calculate_streak(dates):
    if not dates:
        return 0

    today = datetime.today().date()
    yesterday = today - timedelta(days=1)

    sorted_dates = sorted(datetime.strptime(d, "%Y-%m-%d").date() for d in dates)
    streak = 1
    for i in range(len(sorted_dates) - 2, -1, -1):
        if (sorted_dates[i + 1] - sorted_dates[i]).days == 1:
            streak += 1
        else:
            break

    if sorted_dates[-1] == today or sorted_dates[-1] == yesterday:
        return streak
    else:
        return 0

def enrich_user_habits(user_habits):
    for item in user_habits:
        check_ins = item.get("check_ins", [])
        item["streak"] = calculate_streak(check_ins)
        item["checked_in_today"] = date.today().isoformat() in check_ins
    return user_habits

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/dashboard", methods=["POST"])
def dashboard():
    username = request.form.get("username", "").strip().lower()
    user_type = request.form.get("user_type")
    all_habits = load_habits()

    existing_usernames = {h["username"] for h in all_habits}

    if user_type == "returning":
        user_habits = [h for h in all_habits if h["username"] == username]
        if not user_habits:
            return render_template("index.html", error="Username not found. Please try again or register as a new user.")
        user_habits = enrich_user_habits(user_habits)
        return render_template("dashboard.html", habit_data=user_habits, username=username, user_type=user_type)

    if username in existing_usernames:
        return render_template("index.html", error="That username already exists. Please choose a different name.")

    # Handle new user habit selection
    habits = []
    for i in range(1, 4):
        dropdown = request.form.get(f"habit{i}", "").strip()
        custom = request.form.get(f"custom{i}", "").strip()
        final_habit = custom if dropdown == "Custom" and custom else dropdown
        if final_habit:
            habits.append(final_habit)

    user_habits = []
    for habit in habits:
        message = generate_motivation_for_habit(habit)
        user_habits.append({
            "username": username,
            "habit": habit,
            "message": message,
            "check_ins": [],
            "status": "active"
        })

    all_habits.extend(user_habits)
    save_habits(all_habits)

    user_habits = enrich_user_habits(user_habits)
    return render_template("dashboard.html", habit_data=user_habits, username=username, user_type=user_type)

@main.route("/checkin", methods=["POST"])
def checkin():
    username = request.form.get("username")
    habit_to_check = request.form.get("habit")
    today = date.today().isoformat()

    habit_data = load_habits()

    for item in habit_data:
        if item["username"] == username and item["habit"] == habit_to_check:
            if "check_ins" not in item:
                item["check_ins"] = []
            if today not in item["check_ins"]:
                item["check_ins"].append(today)

    save_habits(habit_data)

    user_habits = [h for h in habit_data if h["username"] == username]
    user_habits = enrich_user_habits(user_habits)
    return render_template("dashboard.html", habit_data=user_habits, username=username, user_type=user_type)

@main.route("/master", methods=["POST"])
def master():
    username = request.form.get("username")
    habit_to_master = request.form.get("habit")

    habit_data = load_habits()

    for item in habit_data:
        if item["username"] == username and item["habit"] == habit_to_master:
            item["status"] = "mastered"

    save_habits(habit_data)

    user_habits = [h for h in habit_data if h["username"] == username]
    user_habits = enrich_user_habits(user_habits)
    return render_template("dashboard.html", habit_data=user_habits, username=username, user_type=user_type)

@main.route("/replace", methods=["POST"])
def replace():
    username = request.form.get("username")
    old_habit = request.form.get("old_habit")
    new_habit = request.form.get("new_habit")
    custom_habit = request.form.get("custom_habit")

    final_habit = custom_habit if new_habit == "Custom" and custom_habit else new_habit
    if not final_habit:
        return redirect(url_for("main.index"))

    habit_data = load_habits()

    for item in habit_data:
        if item["username"] == username and item["habit"] == old_habit:
            item["status"] = "mastered"

    message = generate_motivation_for_habit(final_habit)
    habit_data.append({
        "username": username,
        "habit": final_habit,
        "message": message,
        "check_ins": [],
        "status": "active"
    })

    save_habits(habit_data)

    user_habits = [h for h in habit_data if h["username"] == username]
    user_habits = enrich_user_habits(user_habits)
    return render_template("dashboard.html", habit_data=user_habits, username=username, user_type=user_type)
