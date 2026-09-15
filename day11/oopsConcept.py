#Example 1: Creating a class along with object
# class Myclass:
#     def myfunc(self):
#         pass
#     def display(self, name):
#         print(name)
# mc1=Myclass()
# mc1.myfunc()
# mc1.display("Shashi")
# mc2=Myclass()
# mc2.myfunc()
# mc2.display("Kumar")

#Example 2: Instance vs Static
#self inside the tatic method is a parameter name, it doesn't refer to object
# class Myclass:
#     def m1(self):
#         print("This is instance method")
#     @staticmethod
#     def m2(self, num):
#         print(self,num)
# mc=Myclass()
# mc.m1()
# mc.m2(10,20)
# Myclass.m2(20,40) #static method can be access directly from class
#
# #Example 3: define the variables inside the class
# class Myclass1:
#     a,b=10,20 #class variable
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=Myclass1()
# mc.add()
# mc.mul()

#Example 4: Local, Global and class variable
# i,j=15,25
#
# class Myclass3:
#     a,b=10,20
#     def add(self,x,y):
#         print(x+y)              #local
#         print(self.a+self.b)    #class
#         print(i+j)              #global
# mc=Myclass3()
# mc.add(100,200)

#Example 5: Local, Global and class variable (same name variables)
# x,y=15,25
# class Myclass3:
#     x,y=10,20
#     def add(self,x,y):
#         print(x+y)              #local
#         print(self.x+self.y)    #class
#         print(globals()['x']+globals()['y'])              #global
# mc=Myclass3()
# mc.add(100,200)

#Example 6: class with constructor
# class Myclass6:
#     def __init__(self):
#         print("This is constructor")
#     def m1(self):
#         print("This is m1 method")
#     def m2(self,a,b):
#         return a+b
# mc=Myclass6()
# mc.m1()
# print(mc.m2(10,20))
#
# #Example 7: Constructor with parameters and variables
# class Myclass7:
#     name="Kumar"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# mc=Myclass7("Shashi")

#Example 8: class with construtor and methods
class Emp:
    def __init__(self,id,ename,salary):
        self.id=id
        self.ename=ename
        self.salary=salary
    def display(self):
        print(self.id,self.ename,self.salary)
e1=Emp(101,"Shashi",50000)
e1.display()
e2=Emp(102,"Kumar",60000)
e2.display()




















