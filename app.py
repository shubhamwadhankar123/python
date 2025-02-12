from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Web App</h1><p>This is a simple Flask application.</p>"

@app.route('/contact')
def contact():
    return "<h2>Contact Us</h2><p>Email: contact@example.com</p>"

if __name__ == '__main__':
    app.run(debug=True)
