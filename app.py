from flask import Flask, render_template, request, flash, redirect, url_for
import threading
import pose_tracker
from datetime import datetime, timedelta
import os
import json
import random
import subprocess

app = Flask(__name__)
app.secret_key = "your_secret_key"
thread = None

# ---------------------- Pose Tracking ----------------------

def run_pose_tracker(exercise):
    pose_tracker.start_exercise(exercise)

# ---------------------- Streak Logic ----------------------

STREAK_FILE = 'streak_data.json'

def load_streak():
    if os.path.exists(STREAK_FILE):
        with open(STREAK_FILE, 'r') as f:
            return json.load(f)
    return {"dates": []}

def save_streak(data):
    with open(STREAK_FILE, 'w') as f:
        json.dump(data, f)

def update_streak():
    data = load_streak()
    today = datetime.now().strftime('%Y-%m-%d')
    if today not in data["dates"]:
        data["dates"].append(today)
        data["dates"] = sorted(set(data["dates"]))[-30:]  # Keep last 30 days
        save_streak(data)

# ---------------------- User Data Log ----------------------

DATA_FILE = "data.json"

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# ---------------------- Routes ----------------------

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        height = float(request.form['height'])  # in cm
        weight = float(request.form['weight'])  # in kg
        water = float(request.form['water'])    # in liters
        sleep = float(request.form['sleep'])    # in hours

        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            suggestion = "You are underweight. Consider strength training and a high-protein diet."
        elif 18.5 <= bmi < 25:
            suggestion = "You have a normal BMI. Maintain with regular cardio and balanced diet."
        else:
            suggestion = "You are overweight. Focus on cardio (HIIT, running) and portion control."

        entry = {
            "name": name,
            "age": age,
            "height_cm": height,
            "weight_kg": weight,
            "water_liters": water,
            "sleep_hours": sleep,
            "bmi": bmi,
            "suggestion": suggestion
        }

        try:
            with open(DATA_FILE, "r") as f:
                all_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            all_data = []

        all_data.append(entry)

        with open(DATA_FILE, "w") as f:
            json.dump(all_data, f, indent=2)

        return f"""
        <body style='background-color:black; color:#39ff14; font-family:sans-serif;'>
                <div style='max-width:600px; margin:100px auto; text-align:center; padding:40px; border:2px solid #39ff14; border-radius:15px;'>
                    <h2>Thanks, {name}!</h2>
                    <p>Your BMI is <strong>{bmi}</strong>.</p>
                    <p>Suggestion: {suggestion}</p>
                    <div style='margin-top:20px;'>
                      <a href="/log" style='color:#39ff14; text-decoration:underline;'>Go Back</a>
                    </div>
                </div>
            </body>
        """


    return render_template("log.html")


@app.route('/start', methods=['POST'])
def start():
    global thread
    exercise = request.form.get('exercise')

    update_streak()

    if thread and thread.is_alive():
        return "Exercise already running!"
    thread = threading.Thread(target=run_pose_tracker, args=(exercise,))
    thread.start()
    return f"Started {exercise}"

@app.route("/diet")
def diet():
    recipes = [
        {
            "name": "Paneer Bhurji",
            "description": "Scrambled paneer with onions, tomatoes, and Indian spices. High in protein and easy to prepare.",
            "calories": 280,
            "image": "paneer_bhurji.jpeg"
        },
        {
            "name": "Chana Salad",
            "description": "Boiled chickpeas mixed with cucumber, onion, tomato, lemon juice and spices. Great post-workout meal.",
            "calories": 220,
            "image": "chana_salad.jpeg"
        },
        {
            "name": "Egg Bhurji",
            "description": "Indian-style scrambled eggs cooked with veggies and spices. Rich in protein and vitamins.",
            "calories": 200,
            "image": "egg_bhurji.jpeg"
        },
        {
            "name": "Moong Dal Cheela",
            "description": "Protein-packed savory pancakes made from moong dal. Light and nutritious breakfast.",
            "calories": 180,
            "image": "moong_dal_cheela.jpeg"
        },
        {
            "name": "Grilled Chicken Tikka",
            "description": "Boneless chicken marinated in yogurt and spices, grilled to perfection. Lean protein meal.",
            "calories": 300,
            "image": "chicken_tikka.jpeg"
        }
    ]
    return render_template("diet.html", recipes=recipes)

@app.route('/motivation')
def motivation():
    quotes = [
        {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
        {"text": "The pain you feel today will be the strength you feel tomorrow.", "author": "Arnold Schwarzenegger"},
        {"text": "What seems impossible today will one day become your warm-up.", "author": "Unknown"},
        {"text": "Success starts with self-discipline.", "author": "David Goggins"},
        {"text": "Discipline is choosing between what you want now and what you want most.", "author": "Abraham Lincoln"},
    ]
    return render_template("motivation.html", quote=random.choice(quotes))

@app.route('/streak')
def streak():
    data = load_streak()
    today = datetime.utcnow().date()
    streak_count = 0

    for i in range(len(data["dates"]) - 1, -1, -1):
        d = datetime.strptime(data["dates"][i], "%Y-%m-%d").date()
        if (today - d).days == streak_count:
            streak_count += 1
        else:
            break

    return render_template("streak.html", streak=streak_count, dates=data["dates"], datetime=datetime, timedelta=timedelta)

@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@app.route('/reaction-dodge-game')
def reaction_dodge_game():
    return render_template('reaction_dodge_game.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/exercise/<name>')
def start_exercise(name):
    valid_exercises = ['squats', 'pushups', 'bicep-curls', 'bench-press', 'sitting-posture']
    if name not in valid_exercises:
        return "Invalid Exercise", 404

    subprocess.Popen(['python', 'exercise_pose.py', name])
    return f"<h2>Starting {name.replace('-', ' ').title()}... Check the webcam window!</h2>"

# ---------------------- Run ----------------------

if __name__ == '__main__':
    app.run(debug=True)
