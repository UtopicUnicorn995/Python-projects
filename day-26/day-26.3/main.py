##PYTHON EXERCISE

# get the common numbers in 2 files

read1 = open("./file1.txt", "r")

file1 = [int(number.rstrip()) for number in read1]
print(file1)


with open("file2.txt") as file2:
    file_2_data = file2.readlines()

print(file_2_data)

# result = list(set(file1) & set(file2))
result = [set1 for set1 in file1 if set1 in [int(set2) for set2 in file_2_data]]
print(result)
