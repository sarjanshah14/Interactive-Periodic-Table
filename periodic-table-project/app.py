from flask import Flask, render_template
from element_data import elements

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", elements=elements)

@app.route("/faqq")
def faqq():
    # Static FAQs for now (replace later if needed)
    faqs = [
        {
            "question": "What is the periodic table?",
            "answer": "The periodic table is a chart that organizes chemical elements based on atomic number and properties."
        },
        {
            "question": "Who created the periodic table?",
            "answer": "Dmitri Mendeleev created the first widely recognized periodic table."
        },
        {
            "question": "What is an atomic number?",
            "answer": "The atomic number is the number of protons in an atom."
        }
    ]
    return render_template("faqq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)
