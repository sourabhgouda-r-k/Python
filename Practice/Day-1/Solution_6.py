print("Enter the integer number to find positive, negative or zero")
num = int(input("Enter the number: "))
if num < 0:
    print(f"{num} is negative")
elif num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is zero")
