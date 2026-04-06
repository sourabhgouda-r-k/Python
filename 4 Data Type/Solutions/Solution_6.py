# Type Confusion
a = "10"
b = 5
# print(a + b)  error: {can only concatenate str (not "int") to str}

print(int(a) + b)  # will add and give sum
# or
print(a + str(b))  # will concatenate both string
