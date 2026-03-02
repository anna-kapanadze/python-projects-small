import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter rock, paper or scissors: ").lower()

if player == computer:
    print("It's a draw! You both picked " + computer)
elif player == "rock" and computer == "scissors":
    print("You win!!! Rock beats scissors")
elif player == "paper" and computer == "rock":
    print("You win!!! Paper beats rock")
elif player == "scissors" and computer == "paper":
    print("You win!!! Scissors beats paper")
else:
    print("You lose... Computer picked " + computer)
