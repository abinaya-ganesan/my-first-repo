with open("notes.txt", "r") as file, open("notes2.txt", "w") as file2:
    for line in file:
        print(line)
        file2.write(line)

print("I made it! I'm a millionaire now")