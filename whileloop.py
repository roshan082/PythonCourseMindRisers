# while loop
# the iteration over a block of code as long as the condition is true..

#syntax
    # while condiction:
    #   expression or loop body

# example: 

num = 34
while num == 34:
    print("Is greater...")
    #(if loop is infinite use break to stop loop)
    break

x = 1
while x <= 10:
    print(x)
    # equivalent to x = x + 1
    x += 1


# iterative objects
items = ["Heater", "Light", "Fan", "Door Bell", "Bucket"]
i = 0
while i < len(items):
    if i == 2 and "Fan" in items[i]:
        print(items[i], "is available in Index", i)
    else:
        print("Items: ", items[i], "Index: ", i)
    i += 1

# else with while
# syntax
numSet = {2, 4, 6, 8, 10}
i = 2
while i <= (len(numSet) + 5):
    if i == 10 and i in numSet:
        print(10, "Is Available..")
    else:
        print(i)
    i += 2
else:
    print("Loop ended")
    for i in range(10):
        print(i) 

# break, continue and pass
# break -- to stop loop or iteration
# continue -- to continue the process till end or certain points
# pass -- to ignore the statement


print("Continue")
i = 0
while i <= 50:
    if i == 20:
        i += 2
        print("number is: ", i)
        continue
    else:
        i += 5
        print("number is: ", i)
        if i >= 32:
            break 

for i in range(10):
    if i == 3:
        print(i)
    if i == 4:
        pass
        print(i)
    print(i)

