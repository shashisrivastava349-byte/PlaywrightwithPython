#Creating Tuple (Immutable)

# mytuple=(10,20,30,40)
# print(mytuple)

#Access tuple elements/values
test=(10,20,30,40, "Shashi", "Kumar", "Shashi", 20)
# print(test)
# print(test[0])
# print(test[1])
# print(test[-1])

#count repeated values
# print(test.count("Shashi"))
# print(test.count("Kumar"))

#Range of indexes
# print(test[2:5])
# print(test[-3:-1])

#change the value in a tuple (not possible)
#by changing tuple in list we can achieve changes
# test[3]="wow"
# print(test)

#tuple-->list-->tuple
# mylist=list(test)
# print("After converting into list :", mylist)
# mylist[1]="Apple"
# print("After changing value list is:", mylist)
# test=tuple(mylist)
# print(test)

#Retrieve data from tuple using loop
# for i in test:
#     print(i)

#Searching item in tuple
if "Shashi" in test:
    print("Exist")
else:
    print("Not Exist")

#len() - count number of values in tuple
print(len(test))

#Adding . Removing values from tuple not allowed - TypeError

#copying the tuple
# test2=test
# print(test2)

#joining tuples
test2=(10,30,90)
joined=test2+test
print(joined)













