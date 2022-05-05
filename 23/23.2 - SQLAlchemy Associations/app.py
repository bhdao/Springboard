from operator import concat
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)

app.debug = True;
app.config['SECRET_KEY'] = '123SECRETKEY4ME'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


connect_db(app)
db.drop_all()
db.create_all()

defaultData = [
  User(first_name='Kirby', last_name = 'Poyo', image_url = 'https://play.nintendo.com/images/Masthead_Kirby.17345b1513ac044897cfc243542899dce541e8dc.9afde10b.png'),
  User(first_name='Meta', last_name = 'Knight', image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM6R5Qn6wwyu4DnJZKJoNJu1_r6kWPGFSzYEU6lH6ioGJ3O6S7sG0kIg_enDFGzzGpxus&usqp=CAU'),
  User(first_name='Tokichurro', last_name = 'Nioh 2', image_url = 'https://i.ytimg.com/vi/l-cpuEBIpIA/maxresdefault.jpg'),
  Post(title='Poyo!',
      content='Poyo poyo poyo 🍅',
      created_at = '2022-05-02 18:19:20',
      user_id = 1
      ),
  Post(title='Poyo\?',
      content='Poyo poyo 🐧 poyo',
      created_at = '2022-05-02 18:19:21',
      user_id = 1
      ),
  Post(title='What is a Poyo?',
      content='I cannot fathom what in Dreamland Kirby is talking about.',
      created_at = '2022-05-03 6:19:21',
      user_id = 2
      ),
  Post(title='My name is Tokichiro.',
      content='Oh yeah I know a Hiddy-- hidEOUS! HAAAA, GOTTEM.',
      created_at = '2020-03-12 00:00:3',
      user_id = 3
      ),

]

for row in defaultData:
  db.session.add(row)

db.session.commit()

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
  return render_template('user.html', user=user, posts=user.posts)

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

@app.route("/posts/<int:post_id>/delete")
def delete_post(post_id):
  Post.query.filter_by(id=post_id).delete()
  db.session.commit()

  return redirect(f'/')

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
  user = User.query.get_or_404(user_id)
  return render_template('edit.html', user = user)

@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
  post = Post.query.get_or_404(post_id)
  return render_template('editpost.html', post = post)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def confirm_edit_user(user_id):
  editing_user = User.query.get_or_404(user_id)
  editing_user.first_name = request.form["first_name"]
  editing_user.last_name = request.form["last_name"]
  editing_user.image_url = request.form["profile_pic"]
  db.session.add(editing_user)
  db.session.commit()
  return redirect(f'/users/{editing_user.id}')

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def confirm_edit_post(post_id):
  editing_post = Post.query.get_or_404(post_id)
  editing_post.title = request.form["title"]
  editing_post.content = request.form["content"]
  db.session.add(editing_post)
  db.session.commit()
  return redirect(f'/users/{editing_post.id}')

@app.route("/posts/<int:post_id>")
def view_post(post_id):
  post = Post.query.get_or_404(post_id);

  return render_template('view_post.html', post=post)

@app.route("/users/<int:user_id>/posts/new")
def new_post(user_id):
  user = User.query.get_or_404(user_id)

  return render_template('newpost.html', user=user)