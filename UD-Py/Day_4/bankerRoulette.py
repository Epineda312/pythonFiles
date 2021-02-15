import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

person_who_pays = random.choices(names)
print(f"{person_who_pays} will be paying for dinner!")

# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items -1)
# person_who_pays = names[random_choice]