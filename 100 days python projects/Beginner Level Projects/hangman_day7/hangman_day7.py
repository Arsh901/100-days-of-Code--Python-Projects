import random

import hangman_words
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_arts
print(hangman_arts.logo)
display = []
for _ in range(word_length):
    display += "_"
print(str(display))

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    

    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.\n")
            print(chosen_word,"was the actual word.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    stages = hangman_arts.stages
    print(stages[lives])