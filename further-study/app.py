from flask import Flask, request, render_template

from stories import fairy_tale, computers

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route('/')
def choose_story():
    return render_template('home.html')
