import os
import sys

# Serverless compatibility: add current directory to path
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if _CURRENT_DIR not in sys.path:
    sys.path.insert(0, _CURRENT_DIR)

from flask import Flask, render_template
from element_data import elements

app = Flask(__name__)

# Configure paths dynamically for serverless
app.template_folder = os.path.join(_CURRENT_DIR, "templates")
app.static_folder = os.path.join(_CURRENT_DIR, "static")

@app.route("/")
def index():
    return render_template("index.html", elements=elements)

@app.route("/faqq")
def faqq():
    faqs = [
        {"id": 1, "question": "What is the periodic table?", "answer": "Organizes chemical elements by atomic properties."},
        {"id": 2, "question": "Who created it?", "answer": "Dmitri Mendeleev in 1869."},
        {"id": 3, "question": "What is atomic number?", "answer": "Number of protons in an atom."}
    ]
    return render_template("faqq.html", faqs=faqs)

