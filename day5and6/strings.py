#Ctreating strings in 3 approaches

#Approach 1: Using double quotes
# name="Shashi"
# grade="A"
# print(name)
# print(grade)

#Approach 2: Using single quotes
# name='Shashi'
# grade='A'
# print(name)
# print(grade)

#Approach 3: Using constructor
# name=str()  #empty string
# grade=str()

# name=str("Shashi")
# grade=str("A")
# print(name)
# print(grade)
# print(type(name))

# + and * operators with strings
# str="Shashi"
# print(str + " Programming")
# print(str * 3)

#slicing strings
#starting index count from 0
#ending index start from 1

# mystring = "Hello World"
# print(mystring[1:3])
# print(mystring[:5])
# print(mystring[2:])
# print(mystring[1:-1])
# print(mystring[-3:-2])

#Formatting string
#F-string is used for formatting string
#put an 'f' in front of the string literal and add curly brackets {} as placeholders for variables and other operation

# Example 1:
# age=34
# # str="My name is Shashi, I am" +age #TypeError
# str= f"My name is Shashi, I am {age}"
# print(str) #print(f"My name is Shashi, I am {age}")

# Example 2: output: The price is 55.00
# price=55
# str=f"The price is {price:.2f}"
# print(str)
#
# # Example 3
# price=30
# str=f"The price is {price*2}"
# print(str)

#in operator with string returns boolean value
str="welcome"
print("come" in str)
print("lome" in str)
print("we" in str)














