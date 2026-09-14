#Example 1: Global and Local Variable
x=20
def myfun():
    y=10
    print(x)
    print(y)
    print(x+y)
myfun()
print(x)

#Example 2:
x=500
def myfun2():
    x=900
    print(x)
myfun2()
print(x)

#Example 3:
y=100
def myfun3():
    global y
    y=200
    print(y)
myfun3()
print(y)

#Example 4:
def myfun4():
    global y
    y=300
    print(y)
myfun4()
print(y)








