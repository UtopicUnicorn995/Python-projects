##PYTHON EXERCISE

# get the common numbers in 2 files

read1 = open("./file1.txt", "r")
read2 = open("./file2.txt", "r")

file1 = [int(number.rstrip()) for number in read1]
print(file1)

file2 = [int(number.rstrip()) for number in read2]
print(file2)

# result = list(set(file1) & set(file2))
result = [set1 for set1 in file1 if set1 in [set2 for set2 in file2]]
print(result)
