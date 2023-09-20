#!/usr/bin/env python3

def quizz(questions:list[str],answers:list[str],chances:int):

    user_answers = [None] * len(questions)
    print("Welcome to my Quizz !!\nYou have 3 chances.")
    for i in range(len(questions)):   #### loop for questions in question to remove all [i]s
        if chances > 0:
            user_answers[i] = input(questions[i])
            while answers[i] != user_answers[i].lower():
                    chances -= 1
                    if chances > 0:
                        print(f"Your answer : {user_answers[i]}")
                        print('Too bad! That is not the correct answer')
                        print(f"You have {chances} chances left")
                        user_answers[i] = input(questions[i])
                    else: 
                        print(f"Your answer : {user_answers[i]}")
                        print("Sorry, you have 0 chances left")
                        print("Oh no, you lost the quiz...")
                        break
            else: 
                print(f"Your answer : {user_answers[i]}")
                print('Good job! This is the right answer')
    if chances > 0:
        print("Congratulations, you win!")
 
q = ['Who is the best superhero?', "What rhymes with tomato?", "Cats or dogs?","Hello?"]

a = ['batman', 'potato', 'dogs','world']

quizz(q, a, chances = 4)