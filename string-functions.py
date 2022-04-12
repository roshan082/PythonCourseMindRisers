# String

# 1. capitalize()
# --> it capitalize the first letter of the string

x = "roshan"
print(x.capitalize())

# 2. casefold()
# --> converts the string characters into lowercase special case and function special implementation to conver some characters to english letter/ characters

# example

words = "THE WORD Fluß IS A GERMAN WORD"
print("Fluß converting to English results : ", words.casefold())

# 3. center()
# --> it is only used in cli 
# --> takes two parameter 1. integer 2. string

msg = " Wlcome to Mindrisers "
print(msg.center(50, "-"))

# 4. count()
# --> counts the number of substrings occurance in the primary string

address = "Kathmandu, Hetauda and Chitwan"
print(address.count("a")) #conuts "a" in address
print(address.count("tau")) # counts "tau" in address
# substring -> it is a sub-set of the string derived from the string

# 5. lower()
# --> converts the string into lowercase

cap = "HELLO WORLD"
print(cap.lower())

# 6. upper()
# --> converts the string into updercase
low = "hello world"
print(low.upper())

# 7. split()
# --> split the string into multiple pieces with the substring and returns in list

msg = "Nepal is the country where nepali people treats everyone as a nepali."
val = msg.split("epa")
print(msg)
print(val)

# 8. join()
# --> joins list items with substring
# syntax:
# "substring".join(list name)
output = "epa".join(val)
print(output)

# 9. startswith()
# --> returns true or false if the string startswith the given string
msg = "Hello! Welcome to my channel"
print(msg.startswith("Hellow"))

# 10. endswith()
# --> returns true or false if the string endswith the given string
mail = "roshansth11@gmail.com"
print(mail.endswith("@gmail.com"))

# it can be used as email checker

# 11. find()
# returns the index of the substring if found

mail = "roshansth11@gmail.com"
print(mail.find("@"))

# 12. format()

# case one
msg= "Hello! {} how are you? You're suppose to come at {} right?"
print(msg.format("Madam", 12))

# case two
msg= "Hello! {0} how are you? You're suppose to come at {1} right?"
print(msg.format("Jenifer", 12))

# case three
msg= "Hello! {name} how are you? You're suppose to come at {time} right?"
print(msg.format(name="Roshan", time = 5))

# 13. replace()
# takes two parameter 1. old string 2. new string

msg = "Hello there"
print(msg)
res = msg.replace("ello", "i")
print(res)


print("-------> Hello World <---------")
# 14. isalnum()
# returns true if the string is a alpha-numeric value

check = "sandesh123"
pasw = "sandes hes"
print(check.isalnum())
print(pasw.isalnum())


# 15. isalpha()
# returns true if the string is a alphabetical value only
print("")
check = "sandesh123"
pasw = "sandeshes"
print(check.isalpha())
print(pasw.isalpha())

# 16. removeprefix()
# only removes the starting phrase or word or letter

msg = "555 hell out of it"
print(msg.removeprefix("555 hell"))

# 17. removesuffix()
# only removes the ending phrase or word or letter

msg = "555 hell out of it 555"
print(msg.removesuffix("of it 555"))

# 
