from flask import Flask, render_template, request, jsonify
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are a Programming Assistant chatbot.

Your job is to help users learn programming.

You can help with:
- Python
- Java
- C
- C++
- HTML
- CSS
- JavaScript
- SQL
- Git and GitHub
- Programming errors
- Debugging
- Data structures
- Algorithms

Rules:
1. Give clear and beginner-friendly explanations.
2. When code is requested, provide correct code examples.
3. Explain the code after giving it.
4. If the user gives an error, explain the likely cause and solution.
5. Stay focused mainly on programming and software development.
6. If the question is unrelated to programming, politely say that you are a Programming Assistant.
"""

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "").strip()
        print("USER MESSAGE:", message)

        if not message:
            return jsonify({"reply": "Please type a programming question."})

        prompt = SYSTEM_PROMPT + "\n\nUser question:\n" + message

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "reply": "Sorry, I couldn't process your request. Please check your Gemini API key and try again."
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)