# Dict method
# 
# 1. copy()
# --> copies a shallow copy of primary dictionary

product_details = {"id": 12, "product_title": "Brush", "product_price": 200.00}

print("Product Details: ", product_details)

copy_product = product_details.copy()
print("Copy Product: ", copy_product)



# 2. clear()
# --> removes all items from the dictinary

# clear_product = product_details.clear()
# print("Clear Product: ", clear_product)

# 3. get()
# --> takes key as perameter and return its value
print("Product : ", product_details.get("product_title"))

print("")
# 4. items()
# --> returns key value pair

print(product_details.items())

print("")

# 5. keys()
# --> returns all the keys of the dict

print(product_details.keys())
print("")

# 6. values()
# --> returns all the values of the dictionary

print(product_details.values())
print("")

# 7. pop()
# --> removes the specified key-value and returns value of the key
print("POP : ",product_details.pop('id'))
print(product_details)

# raise KeyError if key is not available in the dict
# print(product_details.pop("name"))

# 8. popitem()
# --> removes the last inserted member and returns them as key-value pair in the tuple.

print("POP item : ",product_details.popitem())
print(product_details)
print("")

# raise KeyError if dict is empty
# print(product_details.popitem())

# 9. setdefault()
# --> takes two parameter 1. keys 2. values
# if we pass single parameter it treats the parameter as key by-default


