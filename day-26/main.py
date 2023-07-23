## LIST COMPREHENSION

numbers = [1, 3, 5, 7]

new_number = [number + 1 for number in numbers]
print(new_number)

# range_value = range(1, 5)
new_values = [range_num * 2 for range_num in range(1, 5)]
print(new_values)

## CONDITIONAL LIST COMPREHENSION
names = ["Alex", "Christian", "Ian", "Eleanor", "Pikachu"]

few_letters_names = [name.upper() for name in names if len(name) > 5]
print(few_letters_names)

##DICTIONARY COMPREHENSION
import random

students_scores = {student: random.randint(60, 100) for student in names}

# passed_students = {
#     student: students_scores[student]
#     for student in students_scores
#     if students_scores[student] >= 75
# }

# Correct version
passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 75
}
print(passed_students)

student_dict = {
    "student": ["James", "Lilith", "Dean", "Gabriel"],
    "score": [40, 50, 29, 2],
}

# Looping through dictionaries:
for key, value in student_dict.items():
    print(value)
    print(key)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for key, value in student_data_frame.items():
#     print(value)


# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    print(row.student)
