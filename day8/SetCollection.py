#Creating Set
myset1={10,20,40,30,50}
myset2={"apple","orange","banana"}
myset3={100,"A","B","C"}
# myset=set() #empty set
# print(myset1)
# print(myset2)
# print(myset3)
# print(myset)

#We can not asscess specific item from the set

#Access data from set using for loop
# for i in myset1:
#     print(i)
# for i in myset2:
#     print(i)

#Searching item/value in set
print("apple" in myset2)
if 50 in myset1:
    print("Exist")

#find length
print(len(myset1))

#Count repeated value/items, sorting the set, reversing set Not Possible since it does
#not allowed duplicates and set is unordered

#Add items into set
#add() - single value, update()- multiple value

print("Before adding", myset2)
myset2.add("Shashi")
print("After adding",myset2)
myset2.update(["Kumar", "Srivastava"])
print("After update",myset2)

#Remove item from the set
#Approach 1: using remove()
myset2.remove("Srivastava")
print(myset2)

#Approach2: using discard() - will not through error if item not exist
myset2.discard("Kumar")
print(myset2)

#Approach 3: pop() remove random item
myset2.pop()
print(myset2)

#Clearing values from the set
# myset2.clear()
# print("After clearing", myset2)

#Delete set
# del myset2
# print("After deletion", myset2)

#Copying set
#Approach 1: copy()
copied=myset2.copy()
print(copied)

#Approach 2: set()
# setcopied=myset2
# setcopied1=set(myset2)
# print(setcopied)
# print(setcopied1)

#Approach 3: using union()
# myset=myset2.union(myset3)
# print(myset)

#Approach 4: using | symbol
myset=myset2|myset3
print(myset)

#Retriving common values from 2 sets
#Approach 1 :- intersection()
# set1={"a","b","c",10}
# set2={10,20,30,"a"}
# commonvalue=set1.intersection(set2)
# print(commonvalue)

#Approach 2 :- using &
set1={"a","b","c",10}
set2={10,20,30,"a"}
commonvalue=set1 & (set2)
print(commonvalue)

















