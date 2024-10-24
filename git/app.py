from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Category, Question

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
       categories = Category.query.all()
       return render_template('index.html', categories=categories)

@app.route('/quiz', methods=['POST'])
def quiz():
       category_id = request.form['category']
       num_questions = int(request.form['num_questions'])
       questions = Question.query.filter_by(category_id=category_id).limit(num_questions).all()
       return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
       score = 0
       total_questions = len(request.form)
       for key in request.form:
           if key.startswith('question_'):
               question_id = key.split('_')[1]
               selected_option = request.form[key]
               question = Question.query.get(question_id)
               if selected_option == question.correct_answer:
                   score += 1

       return render_template('result.html', score=score, total_questions=total_questions)

if __name__ == '__main__':
       app.run(debug=True)
   