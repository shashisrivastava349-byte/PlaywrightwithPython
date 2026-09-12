#isdecimal()
print("123".isdecimal())
print("a@#$".isdecimal())
print("10.5".isdecimal())

#isdigit()
print("123".isdigit())
print("a@#$".isdigit())
print("10.5".isdigit())

#isnumeric
print("123".isnumeric())
print("a@#$".isnumeric())

#split() : spliting string
#Example:1
s="xyz@gmail.com"
l=s.split("@")
print(type(l))
print(l)
print(l[0])
print(l[1])
#print(l[2]) #IndexError:

#Example 2
x="one,two,three"
l=x.split(",")
print(type(l))
print(l)
print(l[0])
print(l[1])
print(l[2])

#startwith() : returns T/F
z="welcome"
print(z.startswith("wel"))
print(z.startswith("Wel"))

#endswith() : T/F
print(z.endswith("me"))

#trimming spaces -> strip(), lstrip(), rstrip()
a="   hello   "
print(a.strip())
print(a.lstrip())
print(a.rstrip())











