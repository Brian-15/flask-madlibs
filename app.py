import stories
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def base_page():
    return render_template("form.html", words=stories.story.prompts)

@app.route("/story")
def generate_story():
    answers = {
        "verb": request.args["verb"],
        "noun": request.args["noun"],
        "place": request.args["place"],
        "adjective": request.args["adjective"],
        "plural_noun": request.args["plural_noun"]
    }
    
    return render_template("story.html", story_body = stories.story.generate(answers))