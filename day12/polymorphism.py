#Example 1: Method overloading (Polymorphism)
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello", name)
#         else:
#             print("Hello")
# obj = Human()
# obj.sayHello()
# obj.sayHello("Shashi")

#Example 2: overloading
class Cal:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
objectofcal = Cal()
objectofcal.add(10,20,30)
objectofcal.add(20,30)
objectofcal.add(30)
objectofcal.add()