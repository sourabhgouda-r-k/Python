num = int(input("Enter the number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

# Printing the Factorial using the while loop
print("Method 2 ")
i2 = 1
fact2 = 1
while i2 <= num:
    fact2 *= i2
    i2 += 1
print(fact2)
