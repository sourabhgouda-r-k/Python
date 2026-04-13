# simple If Statements
age = int(input("Enter Your Age: "))
if age > 18:
    print("Hi you become adult!")


# if-else Statement
if age > 18:
    print("you become adult!")
else:
    print("Your are still amature")


# if-elif-else statement
marks = int(input("Enter Your marks: "))
if marks > 90:
    print("Excellent")
elif marks > 80:
    print("Good")
else:
    print("Below 80 is average")


# nested if
citizen = True
if age > 18:
    if citizen:
        print("Vote is done")


# Loops
# for Loops
for i in (1, 2, 3):
    print(i)

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)
