# Set Method
    # set has most of the method of dictionary
    # set has moslty mathmetics operations
# --> 
# 1. add() --> adds elements to the set
set_a = {"Book", "Place", "Door"}
print(f"Set Before : {set_a}")
set_a.add("Bus")
print(f"Set After : {set_a}")

# 2. copy()
set_a_copy = set_a.copy()
print(f"Set Copy : {set_a_copy}")

# 3. clear()
# set_a_copy.clear()
# print(f"Set Clear : {set_a_copy}")

# 4. union() --> create new set with items of both set
set_one = {2, 3, 4}
set_two = {5, 6, 7}
set_union = set_one.union(set_two)
print(f"Union Set : {set_union}")

# 5. update() --> updates the primary set with the element of secondary set
set_one = {2, 3, 4}
set_two = {5, 6, 7}
print(f"Set 1 : {set_one}")
print(f"Set 2 : {set_two}")
set_update = set_one.update(set_two)
# set_update = set_two.update(set_one)
# print(f"Update Set : {set}")
print(f" Update Set 1 : {set_one}")
print(f" Update Set 2 : {set_two}")

# 6. pop() --> it removes arbitary element from set (random element not chosen by us)

set_one = {2, 3, 4}
set_two = {5, 6, 7}
print(f"Set 1 : {set_one}")
set_one.pop()
print(f" Pop Set 1 : {set_one}")


# if set is empty it throws KeyError

# 7. removes() --> specified element passed as argument must be the member of the set
# if the element is member then it removes otherwise raise KeyError

set_one = {2, 3, 4}
set_two = {5, 6, 7}
set_one.remove(4)
# set_one.remove(5)
print(f"Reove Set 1 : {set_one}")

# 8. discard() --> it removes the element if the element is a member of a set if not do nothing 
set_one = {2, 3, 4}
set_two = {5, 6, 7}
set_one.discard(4)
print(f"Discard Set 1 : {set_one}")
set_one.discard(5)
print(f"Discard Set 1 : {set_one}")


# 9. isdisjoint() --> returns true if the set are not intersect to each other
set_one = {2, 4, 6}
set_two = {1, 3, 5}
set_disjoint = set_one.isdisjoint(set_two)
print(f"Disjoint Set 1 : {set_disjoint}")

# 10. issuperset() --> returns true if the set is a primary set of secondary set
set_one = {2, 4, 6}
set_two = {1, 2, 3, 4, 5, 6}
print(f"Is Superset : {set_one.issuperset(set_two)}")
print(f"Is Superset : {set_two.issuperset(set_one)}")
print("")

# 11. issubset() --> opposite to issuperset()
# returns true if the set ia a subset or secondary set of the primary set
set_one = {2, 4, 6}
set_two = {1, 2, 3, 4, 5, 6}
print(f"Is Subset : {set_one.issubset(set_two)}")
print(f"Is Subset : {set_two.issubset(set_one)}")
print("")


# 12. inersection() --. return the matching or common items from the given set
set_one = {2, 4, 6}
set_two = {1, 2, 3, 4, 5, 6}
print(f"Set One : {set_one}")
print(f"Set Two : {set_two}")
print("")
print(f"Intersection : {set_one.intersection(set_two)}")
print(f"Intersection : {set_two.intersection(set_one)}")
print("")

# 13. intersection_update() --> returns None and by removing all other elements of primary keeps only common/matching elemetnts of the set
set_one = {2, 4, 6, 8, 9}
set_two = {1, 2, 3, 4, 5, 6}

print(f"Set One : {set_one}")
print(f"Set Two : {set_two}")
set_one.intersection_update(set_two)
print(f"Set One after Update : {set_one}")

# 14. difference() --> returns the unmatching elements the primary set
set_one = {2, 4, 6, 8, 9}
set_two = {1, 2, 3, 4, 5, 6}
print(f"difference : {set_one.difference(set_two)}")

# 15. difference_update() --> returns NOne and updates the set with the unmatching elements in the set

set_one = {2, 4, 6, 8, 9}
set_two = {1, 2, 3, 4, 5, 6}
set_one.difference_update(set_two)
print(f"difference_update : {set_one}")

# 16. symmetric_difference() --> returns all the unmatching elements of both sets

set_one = {2, 4, 6, 8, 9}
set_two = {1, 2, 3, 4, 5, 6}
print(f"symmetric_difference : {set_one.symmetric_difference(set_two)}")
print(set_one)

# 16. symmetric_difference_update() --> updates the primary set with the unmatching elements from boths sets

set_one = {2, 4, 6, 8, 9}
set_two = {1, 2, 3, 4, 5, 6}
set_one.symmetric_difference_update(set_two)
print(f"symmetric_difference_update : {set_one}")
