print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# #1st Choice
# choice = input('Your at a cross road. Where do you want to go? "Left" or "Right"\n').lower()
# if(choice == "right"):
#   print("Game Over")
# elif(choice == "left"):
#   #2nd Choice
#   choice = input('You come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#   if(choice == "swim"):
#     print("Game Over")
#   elif(choice == "wait"):
#   #3rd Choice
#     choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n').lower()
#   if(choice == "red"):
#     print("Game Over")
#   elif(choice == "blue"):
#     print("Game Over")
#   elif(choice == "yellow"):
#     print("You Win!")
 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#1st Choice
choice1 = input('Your at a cross road. Where do you want to go? "Left" or "Right"\n').lower()
if(choice1 == "left"):
  #Continue game
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if(choice2 == "wait"):
    #Continue Game
    choice3 = input("You Arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
    if(choice3 == "red"):
      print("It's a room full of fire. Game Over")
    elif(choice3 == "yellow"):
      print("You found the treasure! You Win!")
    elif (choice3 == "blue"):
      print("You got binked. Game Over")
    else:
      print("You chose a door that doesn't exist. Game Over")
  else:
    print("You got attacked by a hungry shark. Game Over!")
else:
  print("You fell in a hole. Game Over!")

  