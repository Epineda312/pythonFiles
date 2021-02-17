#Write your code below this row 👇
# 1. Remember your answer should start from 1 and go up to and including 100. 
# 2. Each number/text should be printed on a separate line.
# > `Your program should print each number from 1 to 100 in turn.` 

# >   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

# >     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

for number in range(1,101):
  if(number % 3 == 0 and number % 5 == 0):
    print("fizzbuzz")
  elif(number % 5 == 0):
    print("buzz")
  elif(number % 3 == 0):
    print("fizz")
  else:
    print(number)