# 🔁 Python Control Flow – Notes



# 🔷 1. Conditional Statements (Decision Making)

## 📌 What is it?

👉 Used to make decisions in a program
👉 Executes code based on conditions



## 🔹 if Statement

python
age = 18

if age >= 18:
    print("You can vote")


✔ Runs only if condition is TRUE



## 🔹 if-else

python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


✔ One block will always execute



## 🔹 if-elif-else

python
marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")


✔ Used when multiple conditions are present



## 🔹 Nested if

python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")


✔ Condition inside another condition



## ⚠️ Important Points

* Indentation is very important
* Use comparison operators: > < == != >= <=
* Use logical operators: and, or, not



# 🔁 2. Loops (Repetition)

## 📌 What is a Loop?

👉 Used to repeat a block of code multiple times



## 🔹 for Loop

python
for i in range(5):
    print(i)


👉 Output:


0 1 2 3 4




## 🔹 range() Function

python
range(start, end, step)


Examples:

python
range(5)        # 0 to 4
range(1, 5)     # 1 to 4
range(1, 10, 2) # 1, 3, 5, 7, 9




## 🔹 while Loop

python
i = 1

while i <= 5:
    print(i)
    i += 1


✔ Runs until condition becomes FALSE



## 🔹 break Statement

python
for i in range(5):
    if i == 3:
        break
    print(i)


👉 Stops the loop



## 🔹 continue Statement

python
for i in range(5):
    if i == 2:
        continue
    print(i)


👉 Skips current iteration



## 🔹 pass Statement

python
for i in range(5):
    pass


👉 Does nothing (placeholder)



# 🎯 Summary

* if → decision making
* for → fixed repetition
* while → condition-based repetition
* break → stop loop
* continue → skip iteration





