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
import random

#Determine which player uses what choice
# user_choice = input("What do you choose? (Type 0 for Rock, 1 for Paper or 2 for Scissors)\n")
# print("-----------------------")
# ai_choice  = random.randint(0, 2)

# #print current choice values
# print("Choice Variable Values\n (0 = Rock) (1 = Paper) (2 = Scissors)")
# print(user_choice)
# print(ai_choice)
# print("---------------------------")

# #convert choice to int
# your_move = int(user_choice)
# ai_move = int(ai_choice)

# #list of available choices
# choices = [rock, paper, scissors]

# #use choice index in list to print players choices
# print(choices[your_move])
# print(choices[ai_move])

# #Knowing the rules of Paper,Scissors,Rock
# #Determine the winner by running choices through conditionals
# if(your_move == 0):
#   if(ai_move == 1):
#     print("You Lose")
#   elif(ai_move == 2):
#     print("You Win")
#   else:
#     print("It is a draw")

# if(your_move == 1):
#   if(ai_move == 0):
#     print("You Win")
#   elif(ai_move == 2):
#     print("You Lose")
#   else:
#      print("It is a draw")

# if(your_move == 2):
#   if(ai_move == 0):
#     print("You Lose")
#   elif(ai_move == 1):
#       print("You Win")
#   else:
#     print("It is a draw")
# choices = [rock, paper, scissors]

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? (Type 0 for Rock, 1 for Paper or 2 for Scissors)\n"))

if(user_choice >= 3) or (user_choice < 0):
  print("you typed an invlaid number, you lose!")
else:
  print(game_images[user_choice])
  ai_choice  = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[ai_choice])
  if(user_choice == 0) and (ai_choice == 2):
    print("You win")
  elif(ai_choice == 0) and (user_choice == 2):
    print("You lose")
  elif(ai_choice > user_choice):
    print("You lose")
  elif (user_choice) > (ai_choice):
    print("You win")
  elif (ai_choice) == (user_choice):
    print("It's a draw")



