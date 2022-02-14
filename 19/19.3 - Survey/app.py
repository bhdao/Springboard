from flask import Flask, render_template, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "supersecretpassword1"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

RESPONSES = []
ACTIVITY = []
QUESTION = []
TITLE = []

@app.route('/')
def home():
    title = "Home"
    currActivity = "Home"
    return render_template('home.html', title=title)

@app.route('/start', methods=["POST"])
def start_and_branch():
    if len(ACTIVITY) == 0:
        ACTIVITY.append(request.form['activity'])
    else:
        ACTIVITY.clear()
        RESPONSES.clear()
        ACTIVITY.append(request.form['activity'])
    return redirect('/select')

@app.route('/select')
def select():
    if ACTIVITY[0] == "personality":
        return redirect('/coming_soon')

    qnum = len(RESPONSES)
    activity = surveys[ACTIVITY[0]]
    title = activity.title
    instructions = activity.instructions
    questions = activity.questions
    if qnum >= len(questions):
        return redirect("/survey/complete")
    return render_template("activity.html", activity = activity, questions = questions,  qnum = qnum, instructions = instructions, title = title)




@app.route('/coming_soon')
def coming_soon():
    return render_template("wip.html")

@app.route('/select/confirm', methods=["POST"])
def handle_response():
    answer = request.form['answer']
    RESPONSES.append(answer)
    return redirect('/select')


# @app.route('/survey_start')
# def survey_start():
#     return redirect('/select')

# @app.route('/survey/q<num>')
# def survey(num):
#     num = num
#     q = "something"
#     answers = "somethingElse"
#     return render_template('base.html', title=title, current_survey_title=currActivity, question = q, answers = answers)

@app.route('/survey/complete')
def survey_complete():
    return render_template("complete.html")

@app.route('/<anything>')
def not_found_404(anything):
    return render_template("404.html")