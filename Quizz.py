#!/usr/bin/env python3

def quizz(questions:list[str],answers:list[str],guesses:int):

    user_answers = None
    print("Welcome to my Quizz !!\nYou have 3 guesses.\n")
    for i in range(len(questions)):   #### loop for questions in question to remove all [i]s
        if guesses > 0:
            user_answers = input(questions[i])
            while answers[i] != user_answers.lower():
                    guesses -= 1
                    if guesses > 0:
                        print('Too bad! That is not the correct answer\n')
                        print(f"You have {guesses} guesses left")
                        user_answers = input(questions[i])
                    else: 
                        print(f"Your answer: {user_answers}")
                        print("Sorry, you have 0 guesses left\n")
                        print("Oh no, you lost the quiz...")
                        break
            else: 
                print('Good job! This is the right answer\n')
    if guesses > 0:
        print("Congratulations, you win!")
        
import os
os.system('clear')

print("First set up the quizz!\n")

q = input("Enter your questions here! Please separate them by a comma: ")
question = q.split(',')
question = [item.strip() for item in question]
question = [item + " \n"for item in question]

a = input("Enter your answers here! Please separate them by a comma: ")
answer = a.split(',')
answer = [item.strip() for item in answer]

if len(question) != len(answer):
    print("You must have as many answers as you have questions!")
else:
    guess = int(input("Enter number of guesses: "))

    os.system('clear')
    print("Great! Are your ready?\n")
    k = input("Press any key to continue\n")
    quizz(question, answer, guess)