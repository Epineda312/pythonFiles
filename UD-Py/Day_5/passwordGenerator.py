#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# arr_list = ['Mysql', 'Mongodb', 'PostgreSQL', 'Firebase']
# for i in range(len(arr_list)):
#     print(arr_list[i], end =" ")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#first try
# password = ""
# for i in range(0, nr_letters):
#   password += letters[random.randint(0, 25)]
# for i in range(0, nr_symbols):
#   password += symbols[random.randint(0, 9)] 
# for i in range(0, nr_numbers):
#   password += numbers[random.randint(0, 8)]
# print(password)

#Better solution
# password = ""
# #nr_letters = 4. range doesn't include 4 when its 4 so we make it + 1
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(f"Before randomization: {password_list}")
random.shuffle(password_list)
print(f"After randomization: {password_list}")

# Another way to make a list a string without a for loop
#final_password = "".join(password_list)

final_password = ""
for char in password_list:
  final_password += char

print(f"Your final password is {final_password}")

