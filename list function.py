# list methods

# 1. append()
# --> ads object at the last index of list
epic_book = ["Hamlet", "Lord of the rings", "Karnali blues"]

epic_book.append('Dunkrick')
print(epic_book)

# 2. copy()
# --> repliates or copies items from primary list to secondary list

new_epic = epic_book.copy()
print("Copied List: ", new_epic)

# 3. extend()
#--> takes one parametre at the end of the primary list
kids_book = ["All in one", "Baby Shark"]
print(" ")
print("Before: ", kids_book)
epic_book.extend(kids_book)
print("Extend: ", epic_book)

# 4. insert()
# --> takes two parameter 1. index number 2. object and adds the object to the respective index passed in the parameter
print("Before: ", epic_book)
print("Total index: ", len(epic_book))
epic_book.insert(0, "Hello World")
print("After Insert: ", epic_book)
print("Total index: ", len(epic_book))

# 5. clear()
# --> removes all the items in list

print("After Insert: ", epic_book)
# epic_book.clear()
print("Total index: ", len(epic_book))

# 6. pop()
# --> removes last index items from list
# --> if index is out of range -> raise IndexError

print("Before POP: ", epic_book)
# to remove last index
epic_book.pop()
print("After POP: ", epic_book)
# to remove specific index from the list
epic_book.pop(2)
print("After POP: ", epic_book)

# 7. remove()
# --> removes the value from the list if available and raise ValueError if not available
print("After POP: ", epic_book)
epic_book.remove("Hamlet")
print("After Remove: ", epic_book)

# 8. count()
# --> count the total number of items / value available in the object

# for string
items = ["Pen", "Color", "Oil", "Oil", "Color", "Color"]
print(items.count("Color"))

# 9. index()
# --> takes value as parameter and returns index

print("Oil is in Index : ",items.index("Oil"))

# 10. reverse()
# --> 
print("Befor Reverse : ", items)
items.reverse()
print("After Reverse : ", items)

# 11. sort()
print("Befor Sort : ", items)
items.sort() #accending order
print("After Sort : ", items)
items.sort(reverse=True) #Descending order
print("After Sort reverse : ", items)
