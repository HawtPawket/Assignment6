# 4. The Quiz Game
# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.



questions = ["What is 1+1?", "What is the current year?", "Who was the first president?", "What is 4x4?"]
score = 0
answer = ["2","2024","George Washington", "16"]


question1 = input("What is 1+1?: ")
if question1 == "2":
    print("Good Job!")
    score += 1
else:
    print("That is incorrect!")

question2 = input("What is the current year?: ")
if question2 == "2024":
    print("Good Job!")
    score += 1
else:
    print("That is incorrect!")

question3 = input("Who was the first president?: ")
if question3.lower() == "george washington":
    print("Good job!")
    score += 1
else:
    print("That is incorrect!")

question4 = input("What is 4x4?: ")
if question4 == "16":
    print("Good job!")
    score +=1
else:
    print("That is incorrect!")



print(f"You finished with a score of: {score}")
