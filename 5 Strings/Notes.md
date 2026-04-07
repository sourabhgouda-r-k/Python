# 🧵 Python Strings \& String Functions

## 📌 What is a String?

A **string** is a sequence of characters (text).

👉 Anything inside quotes is a string:

python
name = "Sourabh"
city = 'India'




## 🧠 String Basics

* Strings are written inside:

  * " " (double quotes)
  * ' ' (single quotes)
* You can also use triple quotes:

python
text = """This is
multi-line string"""




## 🔍 Accessing Characters (Indexing)

python
name = "Python"


|Index|Value|
|-|-|
|0|P|
|1|y|
|2|t|
|3|h|
|4|o|
|5|n|

👉 Example:

python
print(name\[0])  # P
print(name\[3])  # h




## ✂️ String Slicing

python
name = "Python"


python
print(name\[0:3])  # Pyt
print(name\[2:5])  # tho


👉 Format:


\[start : end]




## 🔧 Common String Functions

### 1\. len() – Length of string

python
text = "Python"
print(len(text))  # 6




### 2\. lower() – Convert to lowercase

python
text = "PYTHON"
print(text.lower())  # python




### 3\. upper() – Convert to uppercase

python
text = "python"
print(text.upper())  # PYTHON




### 4\. strip() – Remove spaces

python
text = "  hello  "
print(text.strip())  # hello




### 5\. replace() – Replace text

python
text = "Hello World"
print(text.replace("World", "Python"))




### 6\. split() – Split string

python
text = "apple banana mango"
print(text.split())




## 🔗 String Concatenation

python
first = "Hello"
second = "World"

print(first + " " + second)




## 🔥 f-Strings (Best Way)

python
name = "Sourabh"
age = 21

print(f"My name is {name} and I am {age} years old")


👉 Clean and modern way to print





#### count() 

It is used to count how many times a character or word appears in a string

python 

text = "hello world" 

print(text.count("l")





