# Interactive Periodic Table

A college project: a web page that shows all elements in the standard periodic-table layout, colour-coded by element type. Click an element to see its details, including atomic weight and a short fact. There's also a page of frequently asked questions about the periodic table.

## Tech

Python and Flask, with Jinja2 templates and plain CSS. Set up for Vercel (`vercel.json` routes every request to the Flask app).

## Files

```
api/index.py          Flask app (routes: / and /faqq)
api/element_data.py   element data: name, symbol, number, weight, group, period, type, fact
api/templates/        index.html (table), faqq.html (FAQ)
api/static/           styles.css, faq.css
vercel.json           Vercel routing
```

## Run it locally

```bash
pip install -r requirements.txt
flask --app api/index run      # http://localhost:5000
```
