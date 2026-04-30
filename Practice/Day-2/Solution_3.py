# hint Ascii value of Capital A to Z is 65 to 90
text = input("Enter the word to convert to upper case: ")
upper_case = ""
for i in text:
    if "a" <= i <= "z":
        upper_case += chr(ord(i) - 32)
    else:
        upper_case += i
print(upper_case)
