# Printing String
name = "sourabh"
city = "Dharwad"
text = """ This is a 
multi-line string. """
print(name)
print(city)
print(text)

# Accessing Characters (Indexing)
print(name[3])  # output ->  r
print(city[4])  # output ->  w

# String Slicing
print(name[0:3])  # output -> sou
print(city[4:])  # output -> wad

# String Function in Python
# len() function
print(len(name))
print(len(city))

# lower() Convert to lowercase
print(name.lower())

# upper() Convert to uppercase
print(name.upper())

# strip() Remove spaces
Space_name = "  sourabh  "
print(Space_name)  # prints with space
print(Space_name.strip())  # prints without space
print(Space_name.lstrip())  # removes space from left side
print(Space_name.rstrip())  # removes space from right side


# replace() Replace text
print(name.replace("sourabh", "ramkamal"))  # will replace sourabh with ramkamal

# split() split string
fruits = "apple banana mango"
print(fruits.split())


# string Concatenation
first = "sourabh"
last = "gouda"
print("Full Name:", first + last)
# or
print("Full Name:", first + " " + last)


# f-string
print("my name is ", name, "i am from ", city)  # old way
print(f"My name is {name} i am from {city}")  # using the f-string

# count
print(name.count("b"))
print(city.count("a"))


# printing string mltiple times
print("sourabh " * 4)  # will print sourabh 4 times


# startswith and endswith
print(name.startswith("sou"))
print(city.endswith("wad"))

# find()
print(name.find("s"))  # works same as
