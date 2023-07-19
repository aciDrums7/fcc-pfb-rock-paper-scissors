import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def greeting():
    return "Hi!"


response = greeting()
print(response)

choices = get_choices()
print(choices)

# 1 dictionary
dict = {"name": "beau", "color": "blue"}

# 2 list
food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)


def check_win(player, computer):
    if player == computer:
        return "It's a tie!"


a = 3
b = 5
if a == b:
    print("Yes!!!")
