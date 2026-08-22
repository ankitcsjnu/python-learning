"""
print function() output values on the screen. 
you can pass one value or multiple values separated by commas.
"""
# for comment we use ctrl + / for single line comment and triple quotes for multi line comment.
name="Ankit"
age=26  
gender="male"

print("hello",name,"your age is",age,"and gender is ",gender)

print(name,age,gender,sep="-")
print(name,end="\n")

#f- string formatting
# f-strings are a way to format strings in Python. They allow you to embed expressions inside string literals,
#  using curly braces {}. The expressions are evaluated at runtime and the resulting values are inserted into the string.

print(f"your name is {name}, age is {age+4} years and gender is {gender}")
print(age)
