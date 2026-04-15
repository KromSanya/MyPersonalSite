from flask import Flask, render_template
from flask_talisman import Talisman
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-this")

csp = {
    "default-src": "'self'",
    "script-src": [
        "'self'",
        "https://cdn.jsdelivr.net",
    ],
    "style-src": [
        "'self'",
        "'unsafe-inline'",
        "https://cdn.jsdelivr.net",
    ],
    "img-src": [
        "'self'",
        "data:",
    ],
    "font-src": [
        "'self'",
        "https://cdn.jsdelivr.net",
    ],
}

Talisman(
    app,
    force_https=False,
    strict_transport_security=False,
    content_security_policy=csp,
    content_security_policy_nonce_in=None,
    frame_options="DENY",
    referrer_policy="strict-origin-when-cross-origin",
)

@app.route("/")
def index():
    return render_template("index.html", title="Главная")

@app.route("/about")
def about():
    return render_template("about.html", title="Обо мне")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Проекты")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Контакты")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Страница не найдена"), 404

if __name__ == "__main__":
    app.run(debug=True)