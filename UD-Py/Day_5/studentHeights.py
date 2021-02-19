student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# total_height = int(sum(student_heights))
# avg = round(total_height / len(student_heights))
# print(avg)

# total = 0
# count = 0
# for height in student_heights:
#   total += height
#   count += 1
# avg = round(total / count)
# print(student_heights)
# print(f"The number of student heights given is: {count}")
# print(f"The sum of all given heights is: {total}")
# print(f"The average height is: {avg}")

total_height = 0 
for height in student_heights:
  total_height += height

number_of_students = 0 
for student in student_heights:
  number_of_students += 1

  average_height = round(total_height / number_of_students)
  print(average_height)

