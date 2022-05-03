
from random import randint
import random

# create a game for Rock, Paper and Scissors

# p = ['Rock', 'Paper', 'Scissors']
computer = ["1", "2", "3"]
print(random.choice(computer))
player = False
while not player:
    player = input("RocK = 1, Paper = 3, Scissors = 2: ")
    if player == computer:
        print("That is a Tie!")
    elif player == "1":
        if computer == "3":
            print("You loose! Scissors  covers Rock")
        else:
            print("You win! Rock smashes Scissor")
    elif player == "3":
        if computer == "2":
            print("You loose! Scissors cut Paper")
        else:
            print("You win! paper  covers  Scissors")
    elif player == "2":
        if computer == "1":
            print("You loose...Rock smashes Paper")
        else:
            print("You win! Scissors cut Rock")
    # else:
    # print("That is not a valid play. Check your Spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = ["1", "2", "3"]
