#capitalizae() convert first character to upper case
s="hello"
print(s.capitalize())

#casefold() and lower(): converts string into lower case
s1="Hello"
print(s1.casefold())
print(s1.lower())

#upper() : convert string to upper case
s2="shashi"
print(s2.upper())

#title() : convert first character of each word to upper case
s3="welcome to python"
print(s3.title())

#swapcase() : lower case becomes upper and vice versa
s4="Welcome To Python"
print(s4.swapcase())

#centre() : returns a centered string
str="banana"
print(str.center(10))
print(str.center(10,'*'))

#format() : format specified values in a string
name="Shashi"
print("Hello {}".format(name))

#find() : searches the string for a specified value and returns the position of where it was found
s5="Hello"
print(s5.find("e"))
print(s5.find("l"))
print(s5.find("x"))

#index() : searches the string for a specified value and returns the position of where it was found
s6="Hello"
print(s6.index("e"))
print(s6.index("l"))
#print(s6.index("x")) #ValueError

#count() : returns the number of count a specified value occurs in string
s7="banana"
print(s7.count("a"))
print(s7.count("na"))

#replace : returns a string where a specified value is replaced with a different value
s8="Hello World"
print(s8.replace("World","Shashi"))
print(s8.replace("o","X"))

#isalnum : returns true if all characters in the string are alphanumeric(no punctuation no space, characters)
s9="AB12345"
print(s9.isalnum())
s9="abc "
print(s9.isalnum())

#isalpha() : return true if all characters in the string are in the alphabet
x="ABCDE"
print(x.isalpha())
x="123"
print(x.isalpha())

#isdecimal() : returns true if all the characters are in decimal (0-9)
y="123"
print(y.isdecimal())
y="123.55"
print(y.isdecimal())
















