# Loop
# --> loop is used to do the same task for certain given time.

#  for loop --> to perform certain sequences of iteration for particular liit of time

# syntax
# for value in sequesnce or iterative objects:
#   loop body
# here value is the variable that takes value from the item inside the sequesce on each iterattion

# example:

items = ["Smart phone", "Pager", "Walkie Talkei", "Sound"]

for value in items:
    print(value)

# value = items[0] # 1st iteration
# value = items[1] # 2nd iteration
print( "Day 10")
num = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in numbers:
    print(value)


# sum of numbers in numbers variable
total = 0
for sum in numbers:
    total += sum
    print(total)
print(total)

# In case of dictionary

dict_items = {"ID":12, "Title":"Book", "Price":300}

for val in dict_items:
    print(val)


print( "Day 10")
# for loop with range
# range is mostly used in loops
# len method returns te total numbers in items in the object

book_list = ["Math", "Science", "Nepali", "Computer", "Java"]
print("Total Book List:", len(book_list))

for i in range(len(book_list)):
    print("Index: ", i, "Book Name: ", book_list[i])

for i in range(10):
    print(i)
# displays numbers from 0 to 9.

# printing index and index value of iterative object
# len() -- method to count the lenght of the iterative object
print("Length of items:", len(items))
for i in range(len(items)):
    print("Index: ", i , "Value: ", items[i])


# sum of all numbers between 0-10
total = 0
numbers = {0,1,2,3,4,5,6,7,8,9,10}
for i in numbers:
    total += i
    print("Total: ", total)
print("Grand total: ",total)

# if statement inside loop
for i in numbers:
    if i == 4:
        print(i, "This is my favorite number.")
    print(i)


num_set = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num_set)):
    if i%2 == 1:
        print(i, "is a odd number.")
    else:
        print(i, "is a even number.")


for i in range(len(num_set)):
    if i**i == 4:
        print(f"{i} is a square root of 4")
    
    if i**i == 27:
        print(f"{i} is a square root of 27")


# for loop inside for loop
# made triangle with numbers.
print("-----------------------")
for i in range(1, 10):
    print(" ")
    if i > 1:
        for j in range(1, i):
            print(f"{j}", end= " " )
    print(f"{i}", end= " ")
print(" ")
print("-----------------------")
# else with for loop
#for val in sequence:
#     loop body
# else:
#     expression

#example
ordered_items = ["Apple", "Guava", "Orange", "Pear", "Dragon Fruit"]
for name in ordered_items:
    print("Fruits ordered: ", name)
else:
    print("No more items available.")
for i in range(len(ordered_items)):
    if "Orange" in ordered_items[i]:
        print(ordered_items[i], "Is also a color")
    elif "Dragon Fruit" in ordered_items[i]:
        print(ordered_items[i], "Is is the most expensive fruit.")
    else:
        print("Fruits ordered: ", ordered_items[i])
else:
    print("No more items")

