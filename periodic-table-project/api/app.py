import os
from flask import Flask, render_template
from element_data import elements

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def index():
    return render_template("index.html", elements=elements)

@app.route("/faqq")
def faqq():
    faqs = [
        {"question": "What is the periodic table?", "answer": "It organizes chemical elements."},
        {"question": "Who created it?", "answer": "Dmitri Mendeleev."},
        {"question": "What is atomic number?", "answer": "Number of protons in an atom."}
    ]
    return render_template("faqq.html", faqs=faqs)
