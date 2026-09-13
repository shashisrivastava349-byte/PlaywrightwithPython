# Dictonaries are used to store data values in Key:value pairs

#Creating a dictionary
#Approach 1:
# mydictionary={"brand":"Apple", "model":"17pro", "year":2026}
mydictionary={"brand":"Apple",
              "model":"17pro",
              "year":2026}
print(mydictionary)

#Approach 2: using dict() constructor
mydict=dict(name="Shashi", age=29, city="Seoul")
print(mydict)

# a key can have multiple values
mydic={"brand":"Apple",
              "model":"17pro",
              "year":2026,
       "color":["red","yellow","green"]
}
print(mydic)

# Accessing items from dictionary
#Approach 1:
mydic1={"brand":"Apple",
              "model":"17pro",
              "year":2026,
       "color":["red","yellow","green"]
}
print(mydic1["color"])
print(mydic1.get("brand"))

# Get keys : keys() method will return all the keys in dictionary
# print(mydic1.keys())
#
# #Get values : values() method will return all values in dictionary
# print(mydic1.values())
#
# #Get items : items()
# print(mydic1.items())
#
# #Searching key in dictionary
# if "brand" in mydic1:
#     print("Exists")
# else:
#     print("Not Exist")
#
# #Adding items to the dictionary
# mydic1["month"]="january"
# print(mydic1)
#
# #Updating dictionary
# print("Before updating",mydic1)
# mydic1.update({"month":"february"})
# print("After update", mydic1)
#
# # Removing items from dictionary
# #Approach 1: using pop()
# mydic1.pop("month")
# print("After removing", mydic1)
#
# #Approach 2: popitem() last entered item will removed
# mydic1.popitem()
# print("After using popitem", mydic1)
#
# #Approach 3: del keyword
# del mydic1["model"]
# print("After deleting", mydic1)
#
# # del mydic1    # elete dictionary completely
# # print(mydic1)
#
# #Approach 4: clear()
# mydic1.clear()
# print("After clearing", mydic1)

#Copying the dictionary
#Approach 1: using copy()
copieditem=mydictionary.copy()
print(copieditem)

#Approach 2: using dict()
copied=dict(mydictionary)
print(copied)

#length of dictionary
print(len(copied))

#looping dictionary
# for i in copied:
#     print(i)

#Print all keys
for i in copied.keys():
    print(i)
#print all values
for i in copied.values():
    print(i)
#print all items from dictionary
for i,j in copied.items():
    print(i,j)














