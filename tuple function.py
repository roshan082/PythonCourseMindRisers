# tuple methods

# 1. Count
# --> return the total numbers of items availability inthe tuple


days = ("Sunday", "Monday", "Tuesday")

print(days.count("Sunday"))
# if not available
print(days.count("Thrusday"))

# 2. index()
# --> takes value as parameter and return index of the value

print("Position : ", days.index("Tuesday"))


# if not available raise ValueError
# print(days.index("Thrusday"))

# tuple items can be accessed by using index number as well 
print(days[0])