"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)

  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  image_url = db.Column(db.String(), nullable=False, default="placeholder.png")

class Post(db.Model):
  __tablename__ = "posts"

  id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)
  title = db.Column(db.String(50), nullable=False, default="No Title")
  content = db.Column(db.String(1500), nullable=False, default ="No Content")
  created_at = db.Column(db.DateTime, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship('User', backref="posts")



