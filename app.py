"""kom"""
from flask import Flask
app = Flask(name)
@app.route('/')
def index():
    """kom"""
    return '<h1>Hello WSB! Greetings from Flask!</h1>'
if name == "main":
    app.run(debug=True)
