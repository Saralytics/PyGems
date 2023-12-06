import art
from random import randint

print(art.guess)
print("I am thinking of a number between 1 to 100")

EASY_LEVEL_ATTEMPS = 10
HARD_LEVEL_ATTEMPS = 5
correct_answer = randint(1,100)

def set_difficulty():
    level = input("Choose 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_ATTEMPS
    else:
        return HARD_LEVEL_ATTEMPS

def check_guess(guess):
    if guess == correct_answer:
        print("You have guessed correctly! ")
        return
    if guess > correct_answer:
        print(f"Too high!")
    else:
        print(f"Too low!")

def game():
    attemps = set_difficulty()
    print(f"You have {attemps} attemps to guess the number")
    print("=======================================")

    while attemps > 0:
        attemps -= 1
        guess = int(input("Guess a number, must be integer: "))
        check_guess(guess)
        if attemps > 0:
            print(f"Guess again. \nYou have {attemps} remaining to guess the number")
        else:
            print("You've run out of guesses, you lose")
        
game()
