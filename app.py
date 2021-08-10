import stories
from flask import Flask, request, render_template
app = Flask(__name__)

story_num = None

@app.route("/")
def home_menu():

    return render_template("home.html", story_templates=stories.story_arr)

@app.route("/form")
def form_page():
    stories.story_select = int(request.args["story_select"]) - 1
    story = stories.story_arr[stories.story_select]

    return render_template("form.html",
        story_template=story.template,
        words=story.prompts
    )

@app.route("/story")
def generate_story():
    answers = {**request.args}
    
    return render_template("story.html",
        story_body = stories.story_arr[stories.story_select].generate(answers))