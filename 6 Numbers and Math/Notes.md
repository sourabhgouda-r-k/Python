# 🔢 Python Numbers \& Math - Notes



## 📌 1. Types (Number Conversion \& Checking)

### 🔹 type()

👉 Used to check the data type

python
x = 10
print(type(x))   # <class 'int'>




### 🔹 int()

👉 Convert value to integer

python
x = int(5.7)   # 5




### 🔹 float()

👉 Convert value to decimal

python
x = float(10)   # 10.0




### 🔹 complex()

👉 Used for complex numbers

python
x = complex(2, 3)   # 2 + 3j




## ➕ 2. Math Operators

|Operator|Meaning|Example|
|-|-|-|
|+|Addition|3 + 2 = 5|
|-|Subtraction|3 - 2 = 1|
|\*|Multiplication|3 \* 2 = 6|
|/|Division|3 / 2 = 1.5|
|//|Floor Division|3 // 2 = 1|
|%|Modulus|3 % 2 = 1|
|\*\*|Power|3 \*\* 2 = 9|



## 🔁 3. Rounding Functions

### 🔹 abs()

👉 Gives positive value

python
print(abs(-10))   # 10




### 🔹 round()

👉 Rounds number

python
print(round(4.6))   # 5




### 🔹 ceil() (from math module)

👉 Always rounds UP

python
import math
print(math.ceil(4.2))   # 5




### 🔹 floor() (from math module)

👉 Always rounds DOWN

python
import math
print(math.floor(4.8))   # 4




### 🔹 trunc() (from math module)

👉 Removes decimal part

python
import math
print(math.trunc(4.9))   # 4




## 📐 4. Advanced Math (math module)

python
import math


### 🔹 sqrt()

python
print(math.sqrt(25))   # 5




### 🔹 sin(), cos() (optional) 

python
print(math.sin(0))
print(math.cos(0))




### 🔹 log() (optional)

python
print(math.log(10))




## 🎲 5. Random Module

python
import random


### 🔹 random()

👉 Gives random number between 0 and 1

python
print(random.random())




### 🔹 randint()

👉 Random integer in range

python
print(random.randint(1, 10))




## ✅ 6. Validation Functions

### 🔹 is\_integer()

👉 Checks if float is integer

python
x = 5.0
print(x.is\_integer())   # True




### 🔹 isinstance()

👉 Checks data type

python
x = 10
print(isinstance(x, int))   # True




# 🎯 Summary

* Use type() → check data type
* Use int(), float() → convert data
* Use operators → calculations
* Use math module → advanced math
* Use random → random values
* Use validation → check correctness



# 🚀 Pro Tip

👉 Always remember:

* math functions need → import math
* random functions need → import random



