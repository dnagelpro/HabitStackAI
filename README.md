
# 🧠 HabitStackAI

HabitStackAI is a smart, motivational habit tracker built with Flask and powered by the OpenAI API. It helps users build better lives by stacking habits with personalized, AI-generated encouragement and a clean, mobile-friendly interface.

## 🌟 Features

- 👤 New and Returning User Flow
- ✅ Daily Habit Check-In with Streak Tracking
- 🧠 AI-Generated Motivational Messages (via OpenAI)
- 🪜 Habit Mastery & Replacement System
- 🧾 JSON-Based Data Persistence (per user and habit)
- 📱 Mobile-Friendly Design with Responsive Styling
- 🖼️ Clean UI with Custom Logo and Emoji Enhancements

## 🚀 How It Works

1. **New Users** select up to 3 habits or define custom ones.
2. **Returning Users** are redirected to a personalized dashboard.
3. **Daily Check-Ins** build streaks and prompt motivational messages.
4. **Habits can be Mastered and Replaced**, allowing continued growth.
5. **OpenAI API** provides fresh, inspiring messages each time.

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **OpenAI API**
- **HTML / CSS / Jinja Templates**
- **Dotenv** for secure API key handling

## 📁 Project Structure

```
habitstackai/
├── app/
│   ├── ai/coach.py
│   ├── utils/storage.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── static/
│       ├── style.css
│       └── HabitStackAI.png
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

## 🔐 Environment Variables

Store your OpenAI API key in a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

## 💻 Setup Instructions

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies  
4. Add your `.env` file  
5. Run the app with `flask run`

```
git clone https://github.com/yourusername/habitstackai.git
cd habitstackai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
flask run
```

## 🧠 Motivation Credit

This app uses the OpenAI API to deliver motivational coaching tailored to each habit. Every visit is a fresh dose of inspiration.

---

Built with ❤️ by Dawn using AI-powered tools and a passion for habit transformation.
