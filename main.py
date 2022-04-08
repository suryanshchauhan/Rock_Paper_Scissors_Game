import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

#Choose Rock, Paper or Scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0: 
  sys.exit("You typed an invalid number. Try again")
else:
  print(game_images[user_choice])
  

#Computer Choses: 0 for Rock, 1 for Paper and 2 for Scissors.
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 1:
  print("You lost. Paper covers rock.")
elif user_choice == 0 and computer_choice == 2:
  print("You won.")
elif user_choice == 1 and computer_choice == 2:
  print("You lost. Scissors cuts paper.")
elif user_choice == 1 and computer_choice == 0:
  print("You won.")
elif user_choice == 2 and computer_choice == 0:
  print("You lost. Rock smashes scissors.")
elif user_choice == 2 and computer_choice == 1:
  print("You won.")
elif user_choice == computer_choice:
  print("It is a draw.")
  
