#Example 1: Function with Arbitrary or variable-length Arguments
# def sum_function(*number):
#     sum=0
#     for i in number:
#         sum=sum+i
#     return sum
# print(sum_function(1,2,3,4,5,6))
# print(sum_function(15,20,30))
# print(sum_function())

#Example 2: Function with positional and keyword arguments

# def myfun(i,j):
#     print(i,j)
# # myfun(10,20) #positional arguments
# # myfun(i=100,j=200) # keyword arguments
# myfun(j=100,i=200)  # keyword arguments

#Example 3: Default values can be assigned to positional arguments
def myfun1(i=10,j=20):
    print(i,j)
myfun1(100)
myfun1()

#Example 4: Mixing of both positional and keyword arguments
def myfun(a,b,c):
    print(a,b,c)
# myfun(10,20,30) #positional arguments
# myfun(a=100,b=200,c=300) # keyword arguments
# myfun(a=100,c=200,b=300)  # keyword arguments
myfun(100,200,c=300)

#Example 5: Function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
#print(largest(100,200))
result=largest(a=50,b=220)
print(result)
print(type(result))




















