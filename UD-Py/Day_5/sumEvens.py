total_evens = 0
for number in range(2, 101, 2):
  print(number)
  total_evens += number
print(f"The sum of all even numbers between 1 and 100 is: {total_evens}")
