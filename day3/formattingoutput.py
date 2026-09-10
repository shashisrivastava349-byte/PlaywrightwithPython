# name="Shashi"
# age=34
# sal=500.60

name,age,sal="Shashi",34,500.60

#Approach 1
print(name,age,sal)

#Approach 2
# print("Name is :" +name)  #valid
# print("Age is :" +age)    #invalid
# print("Name is :",name)
# print("Age is :",age)
# print("Salary is :",sal)

#Approach 3  Not in tradition used for knowledge purpose
# %s -> String %d -> int %g -> decimal

# print("Name: %s Age: %d Salary: %g" %(name,age,sal))
# print("Age: %d Name: %s Salary: %g" %(age,name,sal))

#Approach 4 {} using format() function
print("Name : {} Age : {} salary: {}".format(name,age,sal))
