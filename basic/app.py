from flask import Flask, request, render_template
from stories import fairy_tale

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# @app.route('/home')
# def choice():
#     return render_template('choices.html')
@app.route('/')
def home_form():
   answers = fairy_tale.prompts
   return render_template('home.html', answers = answers)

@app.route('/your-story')
def your_story():
    new_story = fairy_tale.generate(request.args)
    return render_template('your-story.html',new_story=new_story)