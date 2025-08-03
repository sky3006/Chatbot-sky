from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Your CV database including hobbies and natural about me
cv_database = {
    "work_experience": [
        "I’m currently working as an ML Developer at FIZ Frankfurter Innovationszentrum Biotechnologie GmbH since 2025, where I develop AI/ML solutions in biotechnology.",
        "Previously, I was a Data Scientist Intern at Groupe LabelVie in Morocco, focusing on customer segmentation and predictive modeling.",
        "I also had the pleasure of lecturing at ITM Baroda University, teaching subjects like Data Structures and Computer Networks.",
        "Before that, I freelanced as a software developer building apps and tools with technologies like Streamlit and Electron.js."
    ],
    "education": [
        "I’m pursuing an MSc in Industry 4.0 & Management at FOM University, Germany.",
        "I completed my Bachelor of Technology in Computer Science & Engineering from ITM (SLS) Baroda University."
    ],
    "skills": [
        "Python", "JavaScript", "Machine Learning", "Deep Learning", "java",
        "Streamlit", "Electron.js", "SQL/NoSQL", "Data Visualization", "Networks","Kotlin", "Java", "C/C++", "HTML/CSS","Data Analysis"
    ],
    "projects": [
        "Developed a data visualization web tool using Streamlit for dataset uploads and ML training.",
        "Built a real-time gesture recognition system using OpenCV, MediaPipe, and YOLOv5.",
        "Created a fraud email detection system with NLP and machine learning techniques."
    ],
    "certifications": [
        "Machine Learning with Python by IBM",
        "Data Analysis with Python by IBM",
        "Applied Machine Learning by University of Michigan",
        "Blockchain Basics by SUNY Buffalo",
        "Big Data, AI, and Ethics by UC Davis"
    ],
    "contact": {
        "email": "vyomrahulthakkar@gmail.com",
        "linkedin": "https://linkedin.com/in/vyom-thakkar306"
    },
    "languages": [
        "English"
    ],
    "about": (
        "I’m passionate about blending management insights with AI/ML expertise to build impactful business solutions. "
        "Besides tech, I enjoy playing chess, badminton, swimming, listening to music, painting, and writing poems."
    )
}

# Natural, friendly greetings replies
greetings = {
    "hi": ["Hey there! How can I help you learn more about me today?", "Hello! What would you like to know about me?"],
    "hello": ["Hi! Feel free to ask me anything about my skills, projects, or background.", "Hello! What can I do for you today?"],
    "hey": ["Hey! Glad you dropped by. Ask me about my experience or hobbies!", "Hi there! How can I assist you today?"],
    "good morning": ["Good morning! Hope you have a fantastic day. How can I help you?", "Morning! Ready to chat about my background or interests?"],
    "good afternoon": ["Good afternoon! What would you like to know about me?", "Hey! I’m here if you want to learn about my work or hobbies."],
    "good evening": ["Good evening! How can I brighten your day with some info about me?", "Evening! Ask me anything about my skills or passions."],
    "how are you": [
        "I'm just a bot, but I'm doing great! How can I assist you?",
        "I'm here and ready to chat about my CV or hobbies!"
    ],
    "what's up": [
        "All good here! Ask me about my projects or interests.",
        "Just hanging out here, ready to answer your questions!"
    ],
    "are you there": ["Yes, I’m here! What do you want to know about me?", "Absolutely! How can I help you today?"]
}

creator_questions = [
    "who made you", "who coded you", "who created you", "who built you", "who developed you"
]

def chatbot_response(user_msg):
    msg = user_msg.lower().strip()

    # Handle greetings naturally
    for greet_key in greetings:
        if greet_key in msg:
            return random.choice(greetings[greet_key])

    # Handle creator question
    for q in creator_questions:
        if q in msg:
            return "I was coded and developed by Vyom Thakkar."

    # Match question keywords to CV sections, with natural phrasing
    if any(x in msg for x in ["work", "experience", "job", "employer"]):
        return "Here's a bit about my work experience:\n" + "\n".join(cv_database["work_experience"])
    if any(x in msg for x in ["education", "degree", "university", "study"]):
        return "Talking about education:\n" + "\n".join(cv_database["education"])
    if any(x in msg for x in ["skill", "technology", "tools", "language", "programming"]):
        return "I have experience with these skills: " + ", ".join(cv_database["skills"]) + "."
    if any(x in msg for x in ["project", "portfolio"]):
        return "Some of my projects include:\n" + "\n".join(cv_database["projects"])
    if any(x in msg for x in ["certification", "certificate", "course", "training"]):
        return "Here are some certifications I have earned:\n" + "\n".join(cv_database["certifications"])
    if any(x in msg for x in ["contact", "email", "linkedin", "reach"]):
        return f"You can reach me at:\nEmail: {cv_database['contact']['email']}\nLinkedIn: {cv_database['contact']['linkedin']}"
    if any(x in msg for x in ["language", "spoken"]):
        return "I’m proficient in: " + ", ".join(cv_database["languages"]) + "."
    if any(x in msg for x in ["about", "profile", "summary", "hobbies", "interests", "passions"]):
        return cv_database["about"]

    # Default fallback response
    return (
        "I'm not sure about that. You can ask me about my work experience, education, skills, projects, certifications, or hobbies!"
    )

# Flask API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

@app.route("/")
def home():
    return "Vyom's friendly CV chatbot API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
