import random

lose = ("You lose!")
win = ("You win!")
draw = ("Draw!")

player_lives = 5
score = 0
computer_lives = 5

while True:
    print("-------------------------------------------------")
    print("Enter 1 for rock, 2 for paper and 3 for scissors! Enter 0 to exit the game!")
    player_choice = input()
    computer_choice = (1, 2, 3)
    computer_choice = random.choice(computer_choice)

    if player_choice == 1 and computer_choice == 2:
        print("You choose rock, computer chooses paper!")
        print (lose)
        player_lives -= 1

    if player_choice == 3 and computer_choice == 1:
        print("You choose scissors, computer chooses rock!")
        print (lose)
        player_lives -= 1

    if player_choice == 2 and computer_choice == 3:
        print("You choose paper, computer chooses scissors!")
        print (lose)
        player_lives -= 1

    if player_choice == 2 and computer_choice == 1:
        print("You choose paper, computer chooses rock!")
        print (win)
        computer_lives -= 1

    if player_choice == 1 and computer_choice == 3:
        print("You choose rock, computer chooses scissors!")
        print (win)
        computer_lives -= 1

    if player_choice == 3 and computer_choice == 2:
        print("You choose scissors, computer chooses paper!")
        print (win)
        computer_lives -= 1

    if player_choice == computer_choice:
        print("You both choose the same thing!")
        print (draw)

    if ((player_choice or computer_choice)!= 1) and ((player_choice or computer_choice)!= 2) and ((player_choice or computer_choice)!= 3):
        print("Enter a valid command!")

    if player_lives ==0:
        print ('You win the game!')
        break

    if computer_lives == 0:
        print ('Computer wins the game!')
        break
