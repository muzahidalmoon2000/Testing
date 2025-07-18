from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}! Welcome to the test app."

if __name__ == '__main__':
    app.run(debug=True)
