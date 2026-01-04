import os
import sys

# Dynamically add the api directory to path for serverless compatibility
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_API_DIR = _CURRENT_DIR

# Add api directory to path for element_data import
if _API_DIR not in sys.path:
    sys.path.insert(0, _API_DIR)

from flask import Flask, render_template

# Import elements from element_data module
from element_data import elements

app = Flask(
    __name__,
    template_folder=os.path.join(_API_DIR, "templates"),
    static_folder=os.path.join(_API_DIR, "static")
)

@app.route("/")
def index():
    return render_template("index.html", elements=elements)

@app.route("/faqq")
def faqq():
    faqs = [
        {"id": 1, "question": "What is the periodic table?", "answer": "The periodic table is a tabular display of the chemical elements, arranged by atomic number, electron configuration, and recurring chemical properties."},
        {"id": 2, "question": "Who created the periodic table?", "answer": "The periodic table was developed by Russian chemist Dmitri Mendeleev in 1869."},
        {"id": 3, "question": "What is an atomic number?", "answer": "The atomic number is the number of protons in the nucleus of an atom of a chemical element."}
    ]
    return render_template("faqq.html", faqs=faqs)

