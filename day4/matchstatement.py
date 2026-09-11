#The match statement is used to perform different actions based on different condition
#Instead of writing many if...else statements, we can ude match statement.
#Example 1:
# day=int(input("Enter your day :"))
# match day:
#     case 1:print("Sunday")
#     case 2:print("Monday")
#     case 3:print("Tuesday")
#     case 4:print("Wednesday")
#     case 5:print("Thursday")
#     case 6:print("Friday")
#     case 7:print("Saturday")
#     case _:print("Invalid week day")

#Example 2: Combine values
day=int(input("Enter your day :"))
match day:
    case 2|3|4|5|6: print("Weekdays")
    case 1|7: print("Weekend")
    case _: print("invalid week ")

