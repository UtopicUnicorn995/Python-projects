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
