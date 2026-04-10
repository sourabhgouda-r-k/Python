# Type Conversiton
num1 = 10
print(type(num1))  # prints the type of num

num2 = 10.2
print(int(num2))  # Convert the float value to int

num3 = 10
print(float(num3))  # convert the int value to float

num4 = complex(2 + 3)  # complex have 2 parts real and imaginary
# 2 is real number and 3 is imaginary number.
print(num4)  # Optional


# Arithmetic Operator
print(10 + 20)  # addition
print(10 - 20)  # Subtraction
print(10 * 20)  # Multiplication
print(5 / 2)  # Division
print(5 % 2)  # modulus
print(5 // 2)  # floor Division
# this is called floor division it removes the decimal part and gives only the whole number
# normal division (/)   5 /  2 = 2.5
# floor division  (//)  5 // 2 = 2
print(3**2)  # power
# num1 is base and num2 is power  3 power 2 = 9.


# rounding Functions
# abs() Gives only the positive number
num5 = -10
print(abs(num5))  # output 10
print(abs(-5.4))

# round() makes the decimal values round
print(round(10.6))  # its greater then .6 it will round it 11 if less round it 10


import math

# ceil() rounds up
print(math.ceil(10.4))  # round always up makes it 11.

# floor() rounds down
print(math.floor(10.7))  # rounds alwaqys down makes it 10.

# trunc() removes decimal part
print(math.trunc(10.3))  # removes the deciaml (.3)


# sqrt() gives squar root
print(math.sqrt(25))
print(math.sqrt(num1))

# optional things to learn
print(math.sin(0))
print(math.cos(0))
print(math.log(10))


# random Random
import random

print(random.random())  # Gives Random number between 0 to 1.

print(random.randint(1, 10))  # prints random number from 1-10 range


# validation function
# is_integer() This will check weather the value is int or not (10.0, .0 is considerd as int)
x = 10.1
print(x.is_integer())


# isinstance() checks the data type and returns true or false.
print(isinstance(num1, float))
