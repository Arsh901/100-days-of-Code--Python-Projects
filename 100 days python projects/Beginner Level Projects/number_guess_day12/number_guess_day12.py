logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. You have to find it.")

import random 
a = random.randint(1,100)

def level_choose():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        chances = 10
    elif level == "hard":
        chances = 5
    else:
        print(f"'{level}' not defined. Please choose between 'easy' and 'hard' only.")
        level_choose()
    return chances

c = level_choose()

def proceed(ch,number):
    false_guess = True
    while false_guess == True:
        print(f"Chances left to guess: {ch}")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            false_guess = False
        else:
            ch = ch-1
            if ch ==0:
                print("You have run out of guesses, you loose.")
                print(f"The actual number was: {number}")
                false_guess = False
            else:
                if guess>0 and guess < number -10:
                    print("Too low. Try Again")
                elif guess>=number-10 and guess<number:
                    print("Low but nearby. Guess again")
                elif guess<101 and guess>number+10:
                    print("Too high. Try again")
                elif guess>number and guess <=number+10:
                    print("High but nearby. Guess Again")
                    
proceed(c,a)