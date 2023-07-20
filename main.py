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
# print(choices)

# 1 dictionary
dict = {"name": "beau", "color": "blue"}

# 2 list
food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)


def check_win(player, computer):
    # print('You chose ' + player + ', computer chose: ' + computer)
    #? f-string
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

isWin = check_win(choices['player'], choices['computer'])
print(isWin)