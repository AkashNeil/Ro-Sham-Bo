#Engineered by Akash Neil

import random

lose = ("You lose!")
win = ("You win!")
draw = ("Draw!")

player_lives = 5
score = 0
computer_lives = 5

while True:
    print("Enter R for rock; P for paper and S for scissors!")

    while True:

        player_choice = input()
        computer_choice = ("R", "P", "S")
        computer_choice = random.choice(computer_choice)

        if player_choice == "R" and computer_choice == "P":
            print("Computer chooses",computer_choice)
            print (lose)
            player_lives -= 1

        if player_choice == "S" and computer_choice == "R":
            print("Computer chooses",computer_choice)
            print (lose)
            player_lives -= 1

        if player_choice == "P" and computer_choice == "S":
            print("Computer chooses",computer_choice)
            print (lose)
            player_lives -= 1

        if player_choice == "P" and computer_choice == "R":
            print("Computer chooses",computer_choice)
            print (win)
            computer_lives -= 1

        if player_choice == "R" and computer_choice == "S":
            print("Computer chooses",computer_choice)
            print (win)
            computer_lives -= 1

        if player_choice == "S" and computer_choice == "P":
            print("Computer chooses",computer_choice)
            print (win)
            computer_lives -= 1

        if player_choice == computer_choice:
            print("Computer chooses",computer_choice)
            print (draw)

        if ((player_choice or computer_choice)!= "R") and ((player_choice or computer_choice)!= "P") and ((player_choice or computer_choice)!= "S"):
            print("Enter a valid command!")

        if player_lives ==0:
            print ('You win the game!')
            break

        if computer_lives == 0:
            print ('Computer wins the game!')
            break
