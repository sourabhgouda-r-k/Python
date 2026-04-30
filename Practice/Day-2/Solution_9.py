text = input("Enter the word: ")
for i in text:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        text.replace(i, "*")
        print(i)
