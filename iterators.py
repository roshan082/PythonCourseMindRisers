# Iterators
    # --> Simply an object that iterates upon itself
    # --> it is mainly used in loops 

# We must use two methods in itertor
# 1. __iter__()
    # --> it generates iterator

# 2. __next__()
    # --> it manually goes through each iteration and returns item of iterator

# iter() --> by default calls __iter__() method
# next() --> 

# example 

items_list =["Bag", "Tools", "Hammer"]

# creating iterators
# 1. By magic function
    #--> needs to call via object
i_2 = items_list.__iter__()
# 2. By direct function
    # --> object should be passed as arguments
i = iter(items_list)

# displaying Data
print(next(i), next(i), next(i))
# print(next(i))
# print(next(i))

print(i_2.__next__())
print(i_2.__next__())
print(i_2.__next__())

# breaking down in for loop
print("----------------------------------------")
for val in items_list:
    print(val)

#items_list = iterable
#val = element

#for element in iterable:
iterator =iter(items_list)

# infinite while loop
while True:
    try:
        val = next(iterator)
    except:
        break
else:
    raise StopIteration

# actually for loop is a infinite while loop