#Example 1:
# class A:
#     def m1(self):
#         print("This is parent class")
# class B(A):
#     def m2(self):
#         print("This is child class")
# inherit=B()
# inherit.m1()
# inherit.m2()

#Example 2: Single inheritance
# class P:
#     x,y=10,20
#     def m3(self):
#         print(self.x+self.y)
# class C(P):
#     a,b=100,200
#     def m4(self):
#         print(self.a+self.b)
# child=C()
# child.m4()
# child.m3()

#Example 3: Multilevel inheritance
# class P:
#     x,y=10,20
#     def m3(self):
#         print(self.x+self.y)
# class C(P):
#     a,b=100,200
#     def m4(self):
#         print(self.a+self.b)
# class D(C):
#     i,j=5,6
#     def m5(self):
#         print(self.i*self.j)
# dobj=D()
# dobj.m3()
# dobj.m4()
# dobj.m5()

#Example 4: Heirarchy inheritance
# class P:
#     x,y=10,20
#     def m3(self):
#         print(self.x+self.y)
# class C(P):
#     a,b=100,200
#     def m4(self):
#         print(self.a+self.b)
# class D(P):
#     i,j=5,6
#     def m5(self):
#         print(self.i*self.j)
# cobj=C()
# cobj.m3()
# cobj.m4()
#
# dobj=D()
# dobj.m3()
# dobj.m5()

#Example 5: Multiple inheritance
# class P:
#     x,y=10,20
#     def m3(self):
#         print(self.x+self.y)
# class C:
#     a,b=100,200
#     def m4(self):
#         print(self.a+self.b)
# class D(P,C):
#     i,j=5,6
#     def m5(self):
#         print(self.i*self.j)
# objectofD=D()
# objectofD.m3()
# objectofD.m4()
# objectofD.m5()

#Example 6: calling parent class method using child class super(), Overriding
# class A:
#     def m1(self):
#         print("This is m1 from parent class")
# class B(A):
#     def m1(self):
#         print("This is m1 from child class")
#         super().m1()
# objectofB=B()
# objectofB.m1()

#Example 7: calling parent class variables using child class super()
# class A1:
#     a,b=10,20
# class B1(A1):
#     i,j=100,200
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
# objectofB1=B1()
# objectofB1.m1(1000,2000)

#Example 8: Overriding variables
# class A:
#     name="Shashi"
# class B(A):
#     name="Kumar"
#     def m(self):
#         print(super().name)
# objectofB=B()
# print(objectofB.name)
# objectofB.m()

#Example 9: Overriding
class Bank:
    def rateofInterest(self):
        return 0
class XBank(Bank):
    def rateofInterest(self):
        return 10
class YBank(Bank):
    def rateofInterest(self):
        return 12
objectofXBank = XBank()
print(objectofXBank.rateofInterest())

objectofYBank = YBank()
print(objectofYBank.rateofInterest())








