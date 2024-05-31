# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

grades =[100, 70, 89, 90, 64, 59]



def averageGrade():
    average = sum(grades) / len(grades)
    print(f"the average grade for the class is {average}")
averageGrade()



def highestGrade():
    highest = max(grades)
    print(f"the hightest grade for the class was {highest}!")
highestGrade()



def lowestGrade():
    lowest = min(grades)
    print(f"the loswest grade in the class was {lowest}")
lowestGrade()

def letterGrade():
    for grade in grades:
        if grade >= 90:
            print("you got an A!")
        elif grade  >= 80:
            print("you got a B!")
        elif grade >=70:
            print("you got a C!")
        elif grade >= 60:
            print("you got a D!")
        else:
            print("you got an F!")
letterGrade()