import stories
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def base_page():
    return render_template("form.html", words=stories.story.prompts)

@app.route("/story")
def generate_story():
    answers = {**request.args}
    
    return render_template("story.html", story_body = stories.story.generate(answers))