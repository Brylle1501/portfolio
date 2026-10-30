import os
from flask import Flask, render_template

app = Flask(__name__)

# Personal & Profile Information
PROFILE = {
    "name": "Kent Brylle L. Alvarez",
    "role": "Web Developer / IT Specialist",
    "tagline": "Crafting clean, responsive web architectures and reliable digital solutions.",
    "location": "Canocotan, Tagum City, Davao del Norte, Philippines",
    "phone": "+63 951-154-2848",
    "phone_raw": "+639511542848",
    "email": "kentbryllealvarez@gmail.com",
    "github": "https://github.com/Brylle1501",
    "bio": (
        "Passionate Web Developer and IT Specialist focused on engineering "
        "high-performance web applications, clean frontend/backend architecture, "
        "and real-world technical solutions. Dedicated to writing maintainable, "
        "modular code and turning functional requirements into elegant user experiences."
    ),
}

# Technical Skills & Tools Matrix
SKILLS = {
    "frontend": {
        "title": "Frontend Development",
        "description": "Building modern, accessible, and responsive user interfaces.",
        "skills": [
            "HTML5",
            "CSS3",
            "Tailwind CSS",
            "Vanilla JavaScript",
            "Responsive Design",
        ],
    },
    "backend": {
        "title": "Backend & Frameworks",
        "description": "Architecting resilient server-side services and APIs.",
        "skills": [
            "Python",
            "Flask",
            "C++",
            "REST APIs",
        ],
    },
    "tools": {
        "title": "Tools & Environments",
        "description": "Version control, deployment pipelines, and developer tooling.",
        "skills": [
            "Git / GitHub",
            "Vercel",
            "VS Code",
            "Linux / Windows Systems",
        ],
    },
}

# Featured Real Projects Showcase (Strictly actual built projects)
PROJECTS = [
    {
        "id": "expenses-tracker",
        "title": "Expenses Tracker",
        "badge": "Full-Stack Web App",
        "description": (
            "Full-stack expense management and budgeting application with local "
            "state handling and clean data visualization."
        ),
        "tags": ["Python", "Flask", "Tailwind CSS", "Vanilla JS"],
        "github_url": "https://github.com/Brylle1501/expenses-tracker-web",
        "live_url": "https://github.com/Brylle1501/expenses-tracker-web",
        "icon": "wallet",
        "highlights": [
            "Real-time expense categorization and dynamic budget balancing",
            "Lightweight client-side state synchronization with vanilla JS",
            "Responsive, distraction-free modern UI with Tailwind CSS",
        ],
    },
    {
        "id": "eldercare",
        "title": "ElderCare (IoT / Healthcare Prototype)",
        "badge": "IoT / Healthcare Prototype",
        "description": (
            "Smart healthcare monitoring assistance prototype designed for "
            "senior support and real-time tracking logic."
        ),
        "tags": ["Dart / Flutter", "Python", "PLpgSQL", "JavaScript"],
        "github_url": "https://github.com/noelbanac/eldercare_rcfms_v2",
        "live_url": "https://github.com/noelbanac/eldercare_rcfms_v2",
        "icon": "activity",
        "highlights": [
            "Sensor telemetry ingestion and threshold monitoring logic",
            "Emergency alert notification dispatch triggers",
            "Intuitive caregiver portal for rapid status overview",
        ],
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
    )


# WSGI entry point for Vercel and local server execution
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

