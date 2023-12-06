from turtle import clear

import art
import game_data

print(art.logo)

data = game_data.data


def user_prompt():
    """Ask for user choice.
    :return: the index of the item user chose"""
    print(f"Compare A: {data[current_higher]['name']}, a {data[current_higher]['description']}, "
          f"from {data[current_higher]['country']}.")
    print(art.vs)
    print(f"Against B: {data[next_position]['name']}, a {data[next_position]['description']}, "
          f"from {data[next_position]['country']}. ")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        return current_higher
    else:
        return next_position


current_higher = 0
next_position = 1
score = 0

while next_position <= len(data):
    i = user_prompt()
    if data[current_higher]["follower_count"] >= data[next_position]["follower_count"]:
        if i == current_higher:
            current_higher = i
            next_position += 1
            score += 1
            print(f"You are right. Current score is {score}")
        else:
            print(f"Wrong. Game over. Current score is {score}")
            break
    else:
        if i == next_position:
            current_higher = i
            next_position += 1
            score += 1
            print(f"You are right. Current score is {score}")
        else:
            print(f"Wrong. Game over. Current score is {score}")
            break
