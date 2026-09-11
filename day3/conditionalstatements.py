#if
#Example 1 : age>=18 eligible

# age=20
# if age>=18:
#     print("Eligible for Vote")

#Example 2 : Check the amount value after Discount

# amount=1500
# discount=0
# if amount>1000:
#     discount=amount*10/100
#
# print("Actual amount after reducing discount :", amount-discount)
#
# amount=500
# discount=0
# if amount>1000:
#     discount=amount*10/100
#
# print("Actual amount after reducing discount :", amount-discount)

#if else condition
#Example 1 : age>=18 eligible

# age=20
# if age>=18:
#     print("Eligible for Vote")
# else:
#     print("Not eligible for Vote")
#
# age=15
# if age>=18:
#     print("Eligible for Vote")
# else:
#     print("Not eligible for Vote")

#Example 2 : Check the Number is even or odd
# num=18
# if num%2==0:
#     print(num,"is even number" )
# else:
#     print(num,"is odd number")
#
# num=17
# if num%2==0:
#     print(num,"is even number" )
# else:
#     print(num,"is odd number")

#if elif else condition
#Example 1 : There are different slabs of discount on cloths
# 20% on amount exceeding 10000,
# 10% on amount between 5000-10000,
# 5% on amount between 1000-5000,
# No discount if amount<1000

# amount=int(input("Enter purchase amount:"))
# print("actual amount", amount)
#
# if amount >=15000:
#     discount=amount*20/100
# elif amount >5000:
#     discount=amount*10/100
# elif amount >1000:
#     discount=amount*5/100
# else:
#     discount=0
#
# print("purchase amount after discount :", amount-discount)

#Example 2 : 1-Sunday 2-Monday

# weeknumber=int(input("Enter weeknumber :"))
#
# if weeknumber==1:
#     print("Week 1 Sunday")
# elif weeknumber==2:
#     print("Week 2 Monday")
# elif weeknumber==3:
#     print("Week 3 Tuesday")
# elif weeknumber==4:
#     print("Week 4 Wednesday")
# elif weeknumber==5:
#     print("Week 5 Thursday")
# elif weeknumber==6:
#     print("Week 6 Friday")
# elif weeknumber==7:
#     print("Week 7 Saturday")
# else:
#     print("Invalid Week Number")

#Nested if else condition
# number=int(input("Enter number :"))
# print("Entered Number is :",number)
# if number%2==0:
#     if number%3==0:
#         print("Divisible by both 2 and 3")
#     else:
#         print("Divisible by 2 but not 3")
# else:
#     if number%3==0:
#         print("Divisible by 3 but not 2")
#     else:
#         print("Not divisible by 2 and 3")

#Short hand if
# a,b=20,10
#
# if a>b:
#     print("a is greater than b")
#
# if a>b:print("a is greater than b")
#
# #Short hand if else (Ternary operator)
# a,b=20,10
#
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")
#
# print("a is greater than b") if a>b else print("b is greater than a")

#AND (Logical operator) with if elif else
# a=20
# b=10
# c=30
# if a>b and a>c:
#     print("a is largest", a)
# elif b>c and b>a:
#     print("b is largest", b)
# else:
#     print("c is largest", c)

#pass
a=10
b=20
if a>b:
    pass
print("a is largest", a)
























