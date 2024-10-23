from models import db, Category, Question
from app import app

with app.app_context():
       db.create_all()

       # Add categories if they don't exist
       if Category.query.count() == 0:
           categories = ['Science', 'Math', 'History', 'Literature']
           for category in categories:
               new_category = Category(name=category)
               db.session.add(new_category)

           questions = [
               ("What is the chemical symbol for water?", "A", "B", "C", "D", "A", 1),
               ("What planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "B", 1),
               ("What is the powerhouse of the cell?", "Nucleus", "Mitochondria", "Ribosome", "Chloroplast", "B", 1),
               ("Who developed the theory of relativity?", "Newton", "Einstein", "Galileo", "Tesla", "B", 1),
               ("What is 2 + 2?", "3", "4", "5", "6", "B", 2),
               ("What is the square root of 16?", "2", "4", "8", "16", "B", 2),
               ("What is 10% of 200?", "10", "20", "30", "40", "B", 2),
               ("What is the value of Pi?", "3.14", "3.15", "3.16", "3.17", "A", 2),
               ("Who was the first president of the United States?", "Lincoln", "Washington", "Jefferson", "Adams", "B", 3),
               ("In what year did World War II end?", "1945", "1946", "1947", "1948", "A", 3),
               ("Who wrote 'Romeo and Juliet'?", "Shakespeare", "Hemingway", "Twain", "Dickens", "A", 4),
               ("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "C", 4),
               ("Which author created the character 'Sherlock Holmes'?", "Arthur Conan Doyle", "Agatha Christie", "J.K. Rowling", "Tolkien", "A", 4),
               ("What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", "B", 1),
               ("What gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "C", 1),
               ("Who painted the Mona Lisa?", "Van Gogh", "Picasso", "Da Vinci", "Monet", "C", 4),
               ("What is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", "B", 3),
               ("What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Quartz", "C", 1),
                              ("Which planet is closest to the sun?", "Venus", "Earth", "Mercury", "Mars", "C", 1),
               ("What is the main ingredient in guacamole?", "Tomato", "Avocado", "Onion", "Pepper", "B", 4),
           ]

           for q in questions:
               question = Question(
                   question_text=q[0],
                   option_a=q[1],
                   option_b=q[2],
                   option_c=q[3],
                   option_d=q[4],
                   correct_answer=q[5],
                   category_id=q[6]
               )
               db.session.add(question)

           db.session.commit()
           print("Database populated successfully.")
   

