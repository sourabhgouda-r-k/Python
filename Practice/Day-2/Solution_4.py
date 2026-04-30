text = input("Enter the word: ")
v_count = 0
c_count = 0
for i in text:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        v_count += 1
    else:
        c_count += 1

print(f"vowels are {v_count}")
print(f"consonants are {c_count}")
