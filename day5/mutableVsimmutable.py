#Mutable : Can be changed after creation(list, dict, set)
#Immutable : can not changed after creation (int, float, tuple, str)

#Example 1:
s1="hello"
print("original string :", s1)
print("Address : ", id(s1))
s1="H"+s1[1:]
print(s1)
print("Address : ", id(s1))