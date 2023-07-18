with open("my_file.txt", mode="r") as file:
    file.write("New fucking content")
    content = file.read()
    print(content)
