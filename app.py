from flask import Flask, render_template_string
import random

app = Flask(__name__)

QUOTES = [
    {"author": "Albert Einstein", "quote": "Imagination is more important than knowledge."},
    {"author": "Marie Curie", "quote": "Nothing in life is to be feared, it is only to be understood."},
    {"author": "Alan Turing", "quote": "Those who can imagine anything, can create the impossible."},
    {"author": "Ada Lovelace", "quote": "That brain of mine is something more than merely mortal."},
    {"author": "Grace Hopper", "quote": "The most dangerous phrase in the language is, 'We've always done it this way.'"},
    {"author": "Isaac Newton", "quote": "If I have seen further it is by standing on the shoulders of giants."}
]

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Quote Generator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding-top: 100px; background: #f0f0f0; }
        .quote-box { background: white; padding: 40px; margin: auto; width: 50%; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
        .quote { font-size: 24px; font-style: italic; margin-bottom: 20px; }
        .author { font-size: 18px; font-weight: bold; }
        button { padding: 10px 20px; font-size: 16px; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="quote-box">
        <div class="quote">"{{ quote['quote'] }}"</div>
        <div class="author">— {{ quote['author'] }}</div>
        <form method="get">
            <button type="submit">Generate Another</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    quote = random.choice(QUOTES)
    return render_template_string(TEMPLATE, quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
