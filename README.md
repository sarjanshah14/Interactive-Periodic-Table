# Interactive Periodic Table

A Flask-based web application that displays an interactive periodic table and a Frequently Asked Questions (FAQ) section.

## Features

-   **Interactive Periodic Table**: Explore chemical elements with details.
-   **FAQ Section**: Learn more about the periodic table and its history.
-   **Responsive Design**: optimized for desktop and mobile viewing.
-   **Serverless Ready**: Configured for easy deployment on Vercel.

## Tech Stack

-   **Backend**: Python, Flask
-   **Frontend**: HTML, CSS, Jinja2 template engine
-   **Deployment**: Vercel (configuration included)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/interactive-periodic-table.git
    cd Interactive-Periodic-Table
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

**Run the application locally:**

```bash
python api/index.py
```

*   The application will be available at `http://localhost:5000`.
*   Access the FAQ page at `http://localhost:5000/faqq`.

## Deployment

### Vercel

This project is configured for deployment on Vercel.

1.  Install Vercel CLI: `npm i -g vercel`
2.  Run `vercel` in the project root and follow the prompts.
3.  The `vercel.json` file handles the rewrites to the Flask application.

## Project Structure

```
Interactive-Periodic-Table/
├── api/
│   ├── index.py          # Main Flask application entry point
│   ├── element_data.py   # Data for the periodic table
│   ├── templates/        # HTML templates (index.html, faqq.html)
│   └── static/           # Static assets (CSS, JS, images)
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
└── README.md             # Project documentation
```
