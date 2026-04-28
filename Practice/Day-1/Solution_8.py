print("Enter the 2 Number: ")
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
if num1 > num2:
    print(f"{num1} is greatest ")
elif num2 > num1:
    print(f"{num2} is greatest ")
else:
    print("Both are equal")
