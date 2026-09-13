#Creating list
mylist=[10,20,30,40,50,60]
mylist1=["Apple", "Shashi", "Kumar", "srivastava", "Mamta", "Kumari", "Sinha"]
mytest2=["A", 10, "Sri", True]
mylist3=list() # will create empty list
# print(mylist)
# print(mylist1)
# print(mytest2)
# print(mylist3)

#Access items/values/objects
# print(mylist1[0])
# print(mylist1[1])
# print(mylist1[-1])
# print(mylist1[-2])
#
# #Access multiple values from a list (list of indexes)
# print(mylist1[3:6])
# print(mylist1[1:-3])
# print(mylist1[-4:-2])
#
# #Change the item value in list
# print("Before change: ", mylist1)
# mylist1[6]="Srivastava"
# print("After Change" ,mylist1)
#
# #loop with list
# for i in mylist1:
#     print(i)
#
# #Searching an item in list
# if "Shashi" in mylist1:
#     print("Yes,Shashi exists")
# else:
#     print("No,Shashi does not exist")
#
# #find length/size of a list
# print(len(mylist))
# print(len(mylist1))
#
# #count number of repeted item in list
# listrepeat=["Shashi", "Kumar", "Shashi"]
# print(listrepeat.count("Shashi"))

#sorting the list
# print("original list :",mylist1 )
# #mylist1.sort() #ascending order
# mylist1.sort(reverse=True) #descending order
# print("sorted values", mylist1)

#Reversing list item
# print("original sorted order list :",mylist)
# mylist.reverse()
# print("reverse sorted order list :",mylist)

#add item append() insert()
# print("original list :",mylist)
# mylist.append(70)
# print("after appendlist :",mylist)

# print("original list :",mylist)
# mylist.insert(3, 80)
# print("after insertlist :",mylist)

#remove() and pop() remove item from the list
#Approach 1:mytest2
# print("Original list :",mytest2)
# mytest2.remove(10)
# print("after removelist :",mytest2)
#
# #approach 2
# mytest2.pop(1)
# print("after pop list :",mytest2)
#
# #Approach 3:
# del mytest2[1]
# print("after del list :",mytest2)
#
# #deleting list
# del mytest2
# print("after del list :",mytest2)

#copying the list
#Approach1 : copy()
test=[10,20,40,30]
# testcopy=test.copy()
# print(test)
# print(testcopy)

#Approach 2: list()
test2=[20,40,33,56]
# test2copy=list(test2)
# print(test2)
# print(test2copy)

#join the list
#Approach 1: using +
# test3=test+test2
# print(test3)

#Approach 2: using for loop
# for i in test2:
#     test.append(i)
# print(test)

#approach 3: using extend()
test.extend(test2)
print(test)






