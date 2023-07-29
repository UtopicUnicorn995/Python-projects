# student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# # Looping through dictionaries:
# for key, value in student_dict.items():
#     # Access key and value
#     pass

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_alphabet = pandas.DataFrame(data)

# print(phonetic_alphabet)
is_on = True
while is_on:
    name = input("What is your name? ").upper()
    try:
        phonetic_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}
        last = [phonetic_alphabets[name_letter] for name_letter in name]
        is_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(last)
# for index, row in phonetic_alphabet.iterrows():
#     print(row[index])


# # Loop through rows of a data frame
# for index, row in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
