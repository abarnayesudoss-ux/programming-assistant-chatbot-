# Programming Assistant Chatbot

A simple programming assistant chatbot built with **Python Flask, HTML, CSS and JavaScript**.

## Features
- Chat-style interface
- Python, Java, C, C++, HTML, CSS and JavaScript topics
- Basic debugging guidance
- Quick question buttons
- Responsive design
- Ready for Render deployment

## Run locally

```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

## Deploy on Render

1. Create a GitHub repository.
2. Upload all project files.
3. Sign in to Render.
4. Create a new Web Service and connect the GitHub repository.
5. Build Command:
   `pip install -r requirements.txt`
6. Start Command:
   `gunicorn app:app`
7. Deploy.

The included `render.yaml` can also be used for deployment configuration.

## Important
This version does not require a Gemini/API key. It uses built-in responses.
