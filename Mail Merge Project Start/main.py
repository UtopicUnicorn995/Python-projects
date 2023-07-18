# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open("./Input/Names/invited_names.txt") as names:
    names = names.read().splitlines()
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letters:
            letter = letters.read()
            new_letter = letter.replace("[name]", name)
            open(f"./Output/ReadyToSend/LetterTo{name}.txt", "x")
            with open(f"./Output/ReadyToSend/LetterTo{name}.txt", "w") as toSend:
                toSend.write(new_letter)
