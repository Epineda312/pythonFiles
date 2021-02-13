print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# lower_name1 = name1.lower()
# lower_name2 = name2.lower()
# true_score1 = 0
# true_score2 = 0
# love_score1 = 0
# love_score2 = 0
# score1 = 0
# score2 = 0

# #Check how many times true appears in first name
# true_score1 = true_score1 + lower_name1.count("t")
# true_score1 = true_score1 + lower_name1.count("r")
# true_score1 = true_score1 + lower_name1.count("u")
# true_score1 = true_score1 + lower_name1.count("e")

# #Check how many times true appears in second name
# true_score2 = true_score2 + lower_name2.count("t")
# true_score2 = true_score2 + lower_name2.count("r")
# true_score2 = true_score2 + lower_name2.count("u")
# true_score2 = true_score2 + lower_name2.count("e")
# score1 = true_score1 + true_score2

# #Check how many times love appears in first name
# love_score1 = love_score1 + lower_name1.count("l")
# love_score1 = love_score1 + lower_name1.count("o")
# love_score1 = love_score1 + lower_name1.count("v")
# love_score1 = love_score1 + lower_name1.count("e")

# #Check how many times love appears in second name
# love_score2 = love_score2 + lower_name2.count("l")
# love_score2 = love_score2 + lower_name2.count("o")
# love_score2 = love_score2 + lower_name2.count("v")
# love_score2 = love_score2 + lower_name2.count("e")
# score2 = love_score1 + love_score2

# print(f"The love score of both these names are {score1}{score2}")

# #For Love Scores **less than 10** or **greater than 90**, the message should be:
# if(score1 < 1 or score1 > 9):
#   print(f"Your score is {score1}{score2}, you two go together like coke and mentos")
# #For Love Scores **between 40** and **50**, the message should be:
# elif(score1 >= 4 and score1 <= 5):
#   print(f"Your score is {score1}{score2}, you two are alright together")
# #Otherwise, the message will just be their score. e.g.:
# else:
#   print(f"Your score is {score1}{score2}")

#refactored solution
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love)) 

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your love score is {love_score}")

  """
1. The `lower()` function changes all the letters in a string to lower case. 
2. The `count()` function will give you the number of times a letter occurs in a string. 
"""