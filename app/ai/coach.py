import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_motivation_for_habit(habit):
    prompt = (
        f"You are a friendly and encouraging AI habit coach. "
        f"Give a short, powerful motivational message (1–2 sentences) to help someone stick with this habit: '{habit}'. "
        f"Make it specific and inspiring."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful and motivational habit coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=60
        )
        return response.choices[0].message.content.strip().strip('"').strip("'")

    except Exception as e:
        return f"Keep showing up for your habit: '{habit}' — you're doing great!"
