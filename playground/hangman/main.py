import random
import hangman_art
import hangman_words

print(hangman_art.logo)
stages = hangman_art.stages
words_list = hangman_words.word_list
# Randomly choose a word
chosen_word = words_list[random.randint(0,len(words_list)-1)]
## Testing code
print(f"Pssst the chosen word is {chosen_word}")

display = []
for _ in chosen_word:
    display += "_"

print(display)

# Repeat the below until all the '_' have been replaced (user won)
# or user have run out of lives

lives = 6
end_of_game = False
prev_guesses = []

while not end_of_game and lives > 0:
    # Ask the user to make a guess
    guess = input("Make a guess: ").lower()

    # Check if the user guess is in the chosen word
    for idx in range(len(chosen_word)):
        if guess == chosen_word[idx]:
            display[idx] = guess
    
    print(display)
    end_of_game = "_" not in display
    
    ## reduce lives by one only if the guess is not in the chosen word
    if guess not in chosen_word:
      if guess in prev_guesses:
        print("You have already guessed the letter and it's wrong")
        print(display)
      else:
        # Print out the ASCII art corresponding to the nuber of lives remaining
        print(f"Sorry you guessed {guess} and it's not in the word, you lose a life")
        print(stages[lives])
        lives -= 1
        prev_guesses += guess

        if lives == 0:
            print("You lose")
            break

    if end_of_game:
        print("You win")
    
    

