from operator import concat
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.debug = True;
app.config['SECRET_KEY'] = '123SECRETKEY4ME'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route("/")
def list():
  title = "Home"
  users = User.query.all()
  return render_template('list.html', title=title, users=users)

@app.route("/users/add")
def new_user_form():
  title="Add a New User"
  return render_template('addform.html', title=title)


@app.route("/users/<int:user_id>")
def view_user(user_id):
  user = User.query.get_or_404(user_id)
  title = user.first_name+" "+user.last_name
  return render_template('user.html', user=user)

@app.route("/", methods=["POST"])
def add_new_user():
  first_name = request.form["first_name"]
  last_name = request.form["last_name"]
  userPic = request.form["profile_pic"]

  new_user = User(first_name=first_name, last_name = last_name, image_url = userPic)

  db.session.add(new_user)
  db.session.commit()

  return redirect(f'/users/{new_user.id}')

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
  User.query.filter_by(id=user_id).delete()
  db.session.commit()

  return redirect(f'/')

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
  user = User.query.get_or_404(user_id)
  return render_template('edit.html', user = user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def confirm_edit_user(user_id):
  editing_user = User.query.get_or_404(user_id);
  editing_user.first_name = request.form["first_name"]
  editing_user.last_name = request.form["last_name"]
  editing_user.image_url = request.form["profile_pic"]
  db.session.add(editing_user)
  db.session.commit()
  return redirect(f'/users/{editing_user.id}')