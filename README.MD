# 🧠 AI Personal Trainer – Your Smart Fitness Coach 🏋️‍♀️

The fitness world is evolving rapidly with AI-powered solutions. This project, **AI Personal Trainer**, brings the power of **computer vision**, **machine learning**, and **real-time feedback** to your workouts — all through your **webcam**.

---

## ❓ Problem We’re Solving

💢 Home workouts lack real-time feedback  
💢 Incorrect form leads to injuries and poor results  
💢 Personal trainers are expensive and not always available  
💢 Most people don’t have fitness equipment or sensors  

---

## ✅ Our Goal

Build a cost-effective, webcam-based AI coach that can:

- 📏 Detect your posture and guide you in real time  
- 🔁 Count reps and estimate calorie burn  
- 🛡️ Prevent injuries with real-time correction  
- 🌍 Make fitness coaching accessible to everyone  

---

## 💡 Key Features

| Feature                         | Description                                          |
|----------------------------------|------------------------------------------------------|
| 📷 Webcam Integration            | No sensors needed — just a standard webcam          |
| 🧍 Pose Detection                | MediaPipe-based real-time body movement tracking    |
| 🔁 Repetition Counting          | Automatic detection of squats, push-ups, etc.       |
| 📊 Dashboard Metrics            | Calories burned, reps, water intake, workout streaks|
| 🗣️ Voice Feedback (optional)    | Audio prompts using `pyttsx3`                       |
| 🔐 Local Tracking               | Data stored using JSON for simplicity               |

---

## ⚙️ Tech Stack

| Category     | Tools Used                                |
|--------------|--------------------------------------------|
| Frontend     | HTML, CSS, JavaScript, Chart.js           |
| Backend      | Python, Flask                             |
| AI / CV      | OpenCV, MediaPipe                         |
| Data Storage | JSON files, LocalStorage                  |
| Voice Output | pyttsx3 (Text-to-Speech) *(optional)*     |

---

## 📈 Results

- 🧍 Accurate **pose detection** via webcam  
- 🔁 Real-time **rep counting** (e.g., squats, push-ups)  
- 📊 Instant **dashboard feedback**: calories, reps, water, streaks  
- 🗣️ Optional **audio guidance** for corrections  
- 💻 Requires only a **web browser and webcam**  

---

## 💪 Why This Matters

✔️ **Smart Coaching** – Improve faster with real-time posture correction  
🛡️ **Injury Prevention** – Bad form is detected and corrected instantly  
🌐 **Universal Access** – No gym gear or trainer needed — just a webcam  

---


1. **Clone the repository**
   ```bash
   git clone https://github.com/SnehalGGujjar/AI-GYM-TRAINER.git
   cd AI-GYM-TRAINER
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in your browser**
   ```bash
   http://127.0.0.1:5000/
   ```






