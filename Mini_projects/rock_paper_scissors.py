import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None #'None' makes the variable an empty container, that does not contain any values.

    while player not in choices: # this sequence of code, prevents the user from inputing wrong anwers to question.
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("player: ",player)
        print("computer: ",computer)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("player: ",player)
            print("computer: ",computer)
            print("Player lose!")
        if computer == "scissors":
            print("player: ",player)
            print("computer: ",computer)
            print("Player wins!")

    elif player == "paper":
        if computer == "scissors":
            print("player: ",player)
            print("computer: ",computer)
            print("Player lose!")
        if computer == "rock":
            print("player: ",player)
            print("computer: ",computer)
            print("Player wins!")

    elif player == "scissors":
        if computer == "rock":
            print("player: ",player)
            print("computer: ",computer)
            print("Player lose!")
        if computer == "paper":
            print("player: ",player)
            print("computer: ",computer)
            print("Player wins!")

    play_again = input("play again? (yes/no): ").lower() #condition determinant

    if play_again == "no": # condition inside the while loop, if the player wants to play the game again.
        break
print("bye!") #exit game.
