from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(50), nullable=False)
       questions = db.relationship('Question', backref='category', lazy=True)

class Question(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       question_text = db.Column(db.String(200), nullable=False)
       option_a = db.Column(db.String(100), nullable=False)
       option_b = db.Column(db.String(100), nullable=False)
       option_c = db.Column(db.String(100), nullable=False)
       option_d = db.Column(db.String(100), nullable=False)
       correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, D
       category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
   
