

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'The solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

game_won = False
while not game_won:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

  print(display)

  if "_" not in display:
    game_won = True
    print("You Win.")
