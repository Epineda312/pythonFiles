student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}
# Write code below to add the grades to student_grades.
for value in student_scores:
    val = student_scores[value]

    # if val >= 91 and val <= 100:
    #   student_grades[value] = "Outstanding!"
    # elif val >= 81 and val <= 90:
    #   student_grades[value] = "Exceeds expectations"
    # elif val > 71 and val <= 80:
    #   student_grades[value] = "Acceptable"
    # else:
    #   student_grades[value] = "Fail"

    # Revised solution
    if val > 90:
        student_grades[value] = "Outstanding!"
    elif val > 80:
        student_grades[value] = "Exceeds Expectations"
    elif val > 70:
        student_grades[value] = "Acceptable"
    else:
        student_grades[value] = "Fail"

# This is the scoring criteria:
# > Scores 91 - 100: Grade = "Outstanding"
# > Scores 81 - 90: Grade = "Exceeds Expectations"
# > Scores 71 - 80: Grade = "Acceptable"
# > Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

print(student_grades)
