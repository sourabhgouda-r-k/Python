text = input("Enter the word: ")

for i in text:
    if i != i[i + 1]:
        print(i)
