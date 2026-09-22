import math
import random

#Assignment 1 

# playing = True
# num = str(random.randint(1, 10))
# print("Welcome to the Number Guessing Game!")
# while playing:
#     guess = input("Guess a number between 1 and 10(You have 3 attempts): ")
#     attempt = 3
#     while attempt > 0:
#         if guess == num:
#             print("Congratulations! You guessed the correct number:", num)
#             playing = False
#             break
#         else:
#             attempt -= 1
#             if attempt > 0:
#                 guess = input(f"Sorry, that's not the correct number. Try again!(You have {attempt} attempts left): ")
#             else:
#                 print("Sorry, you've run out of attempts. The correct number was:", num)
#                 playing = False

#Assignment 2

playing1 = True
while playing1:
    thing = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    rounds = int(input("How many rounds would you like to play? "))
    score = 0
    for _ in range(rounds):
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer = random.choice(thing)
        print(f"You chose {user_choice}, and the computer chose {computer}.")
        if user_choice == "rock" and computer == "scissors":
            print("You win!")
            score += 1
            print("Score(yours):", score)
        elif user_choice == "paper" and computer == "rock":
            print("You win!")
            score += 1
            print("Score(yours):", score)
        elif user_choice == "scissors" and computer == "paper":
            print("You win!")
            score += 1
            print("Score(yours):", score)
        elif user_choice == computer:
            print("It's a tie!")
            print("Score(yours):", score)
        else:
            print("The computer wins!")
            print("Score(yours):", score)
    break   