# dictionary funtions methods


places = {"zip_code": 44600, "city_name": "Kathmandu", "speciality": "Capital of Nepal", "population": 300000}

places_copy = places.copy()
print("Copied Places : ", places_copy)
print("")

# places_clear = places.clear()
# print("Cleared Places : ", places_clear)
print("--------------------------------------")

places_get = places.get("zip_code")
print("Get Places : ", places_get)
print("--------------------------------------")

places_items = places.items()
print("Items Places : ", places_items)
print("--------------------------------------")

places_keys = places.keys()
print("Key Places : ", places_keys)
print("--------------------------------------")

places_values = places.values()
print("Values Places : ", places_values)
print("--------------------------------------")

places_pop = places.pop("zip_code")
print("POP Places : ", places_pop)
print("After POP : ", places)
print("--------------------------------------")


places_popitems = places.popitem()
print("POPitem Places ( last index is removed )  : ", places_popitems)
print("After POPitems : ", places)

print("--------------------------------------")

places_setdefault = places.setdefault("ID", 200)
print("SetDefault Places : ", places_setdefault)
print(places)
print("--------------------------------------")


# if single parameter is passed -> it take values none
places_setdefault = places.setdefault("Student")
print("SetDefault Places : ", places_setdefault)
print(places)
print("--------------------------------------")

# 10. Update
# --> updates the values of the specified key

places_update = places.update({"zip_code": 44622})
print("Update Places : ", places)
print("--------------------------------------")

# if key not available -> adds the key-value as new member of dict
places_update = places.update({"pass_code": 4556})
print("New key values is inserted : ", places)
print("--------------------------------------")


# 11. fromkeys()
# -> takes two parameter 1. iterative object 2. all types

places_fromkeys_set = {"set_one", "set_two", "set_three"}
values = "Set Data"
value = {1, 2, 3}
res = dict.fromkeys(places_fromkeys_set, values)
print(res)
res1 = dict.fromkeys(places_fromkeys_set, value)
print(res1)