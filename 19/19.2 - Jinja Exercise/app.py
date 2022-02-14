import random
from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "verysecretpassword1"
debug = DebugToolbarExtension(app)

rand_story = random.choice(stories)
selected_story = rand_story
story_idx = stories.index(rand_story)

@app.route("/")
def form():
  return render_template('form.html', title="BD Mad Libs - Home", selected_story=rand_story)

@app.route("/story")
def story():
  answers = {}
  flash("This is a flashed message!!!", "warning")
  req = request.args
  for key in req.keys():
    answers[key] = req[key]
  return render_template('story.html', title="BD Mad Libs - Story", answers=answers, story=stories[story_idx])