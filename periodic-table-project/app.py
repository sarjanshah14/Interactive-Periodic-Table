from flask import Flask, render_template
from element_data import elements  # Import the elements list from element_data.py
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', elements=elements)  # Pass the elements list to the template

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="elements"  # Database name
    )

@app.route('/faqq')
def faqq():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query the FAQs
    cursor.execute("SELECT id, question, answer FROM faqs")
    faqs = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    return render_template("faqq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)
